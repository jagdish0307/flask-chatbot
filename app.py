import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  
from code import get_chatbot_response  # Import function from code.py

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # Allow all origins

@app.route("/")
def index():
    return render_template("index.html")  # Make sure the file is in templates/

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = get_chatbot_response(user_input)

    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
