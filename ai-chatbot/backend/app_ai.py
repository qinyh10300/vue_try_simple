from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from SiliconFlow import SiliconFlow

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend
llm = SiliconFlow()

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    # print(question)
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    response = llm._call(prompt=question, model="deepseek-ai/DeepSeek-V2.5", temperature=0.9)
    return response["content"]

if __name__ == '__main__':
    app.run(debug=True, port=5000)