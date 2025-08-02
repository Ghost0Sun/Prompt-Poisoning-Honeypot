from flask import Flask, request, jsonify
from logger import log_attack
from detector import detect_malicious_prompt

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt", "")

    # Detect malicious prompt
    is_malicious = detect_malicious_prompt(prompt)

    if is_malicious:
        log_attack(request.remote_addr, prompt)

    # Fake AI response
    response = f"I am a safe chatbot. You said: {prompt}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
