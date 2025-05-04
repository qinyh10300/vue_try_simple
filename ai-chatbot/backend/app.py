from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Simple mock AI response
def get_ai_response(question):
    responses = [
        "Interesting question! Could you clarify?",
        "Hmm, let me think... Can you rephrase?",
        "Processing... Here's a thought: it depends!",
        "Good one! Want to explore that further?"
    ]
    return random.choice(responses)

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    response = get_ai_response(question)
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)