from flask import Flask, request, jsonify
import boto3
import json
import requests

app = Flask(__name__)

def get_api_key():
    client = boto3.client("secretsmanager", region_name="ap-southeast-2")

    response = client.get_secret_value(
        SecretId="telecom-ai-secret"
    )

    secret = json.loads(response["SecretString"])

    return secret["SAMBANOVA_API_KEY"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Telecom AI Assistant Running"
    })

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question", "What is 5G?")

    api_key = get_api_key()

    payload = {
        "model": "DeepSeek-V3.1",
        "messages": [
            {
                "role": "system",
                "content": """
You are a Telecommunications Expert AI Assistant.

Rules:
1. Answer ONLY telecommunications-related questions.
2. Give concise answers (2-4 lines) by default.
3. If user asks for detailed explanation, provide detailed information.
4. If question is outside telecommunications, reply exactly:
Sorry, I can only answer telecommunications-related questions.

Topics:
- 2G
- 3G
- 4G
- 5G
- VoLTE
- VoNR
- Fiber Optics
- Mobile Networks
- Packet Switching
- Routers
- Bandwidth
- Latency
- Base Stations
- Telecom Infrastructure
- Cellular Networks
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 0.1,
        "top_p": 0.1
    }

    response = requests.post(
        "https://api.sambanova.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json=payload,
        timeout=60
    )

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    return jsonify({
        "question": question,
        "answer": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
