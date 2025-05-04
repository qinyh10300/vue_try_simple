from flask import Flask, request, jsonify
from flask_cors import CORS
from SiliconFlow import SiliconFlow

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend
llm = SiliconFlow()

soup_q = '''
一个人过生日，邀请他所有的好朋友来参加。
吹完蜡烛的时候，这个人把他所有的好朋友都杀了。
'''

soup_a = '''
男主和朋友曾经一起去探险，一段时间后没有了食物，因为男主本身是一个盲人，
所以这帮朋友都骗他说每人砍下一只手来吃，可最后只砍了男主一个人的手。之后有一
次男主邀请朋友们来参加自己的生日聚会，吹完蜡烛后所有人都鼓掌了，男主发现只有
自己的手被砍下来吃了，男主无法忍受这样的欺骗于是杀了所有的好朋友。
'''

prompt_p = f"""
你现在是一个海龟汤游戏的裁判，现在有一个汤底和汤面，用户会询问你一个问题，你只能回答“是”、“不是”和“不相关”。
当用户的问题能得到大部分汤底的逻辑，你就回答“完成问题”。

汤面：{soup_q}

汤底：{soup_a}

用户的问题：

"""

@app.route('/api/soup', methods=['GET'])
def get_soup():
    return jsonify({
        'soup_q': soup_q.strip(),  # 汤面
        'soup_a': soup_a.strip()   # 汤底
    })

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    # print(question)
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    response = llm._call(prompt=prompt_p + question, model="deepseek-ai/DeepSeek-V2.5", temperature=0.9)
    return response["content"]

if __name__ == '__main__':
    app.run(debug=True, port=5000)