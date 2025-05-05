from flask import Flask, request, jsonify
from flask_cors import CORS
from soups import get_soup_by_id, get_all_soups
from SiliconFlow import SiliconFlow

app = Flask(__name__, static_folder='static')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})  # Adjust for Vite's default port

llm = SiliconFlow()

def generate_prompt(soup_q, soup_a, question):
    return f"""
你现在是一个海龟汤游戏的裁判，现在有一个汤底和汤面，用户会询问你一个问题，你只能回答“是”、“不是”和“不相关”。
当用户的问题能得到大部分汤底的逻辑，你就回答“完成问题”。

汤面：{soup_q}

汤底：{soup_a}

用户的问题：{question}
"""

@app.route('/api/soups', methods=['GET'])
def get_soups():
    soups = get_all_soups()
    return jsonify([{"id": s["id"], "title": s["title"]} for s in soups])

@app.route('/api/soup/<int:soup_id>', methods=['GET'])
def get_soup(soup_id):
    soup = get_soup_by_id(soup_id)
    if not soup:
        return jsonify({'error': 'Soup not found'}), 404
    return jsonify({
        'id': soup['id'],
        'title': soup['title'],
        'soup_q': soup['soup_q'],
        'soup_a': soup['soup_a'],
        'image': soup['image'],
        'audio': soup['audio']
    })

@app.route('/api/ask/<int:soup_id>', methods=['POST'])
def ask(soup_id):
    soup = get_soup_by_id(soup_id)
    if not soup:
        return jsonify({'error': 'Soup not found'}), 404
    
    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    prompt = generate_prompt(soup['soup_q'], soup['soup_a'], question)
    response = llm._call(prompt=prompt, model="deepseek-ai/DeepSeek-V2.5", temperature=0.9)
    return response["content"]

if __name__ == '__main__':
    app.run(debug=True, port=5000)