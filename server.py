# from flask import Flask, request, jsonify
# from app import get_chatbot_response

# app = Flask(__name__)

# history = ""  # Global variable to store conversation history

# @app.route("/chat", methods=["POST"])
# def chat():
#     global history
#     data = request.get_json()
#     user_input = data.get("message", "")

#     if not user_input:
#         return jsonify({"error": "No message provided"}), 400

#     # Get chatbot response
#     response = get_chatbot_response(user_input, history)

#     # Update history
#     history += f"\nUser: {user_input}\nAssistant: {response}"

#     return jsonify({"response": response})

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, request, jsonify, render_template
# from app import get_chatbot_response

# app = Flask(__name__)

# history = ""  # Store conversation history

# @app.route("/")
# def index():
#     return render_template("index.html")  # Load the HTML page

# @app.route("/chat", methods=["POST"])
# def chat():
#     global history
#     data = request.get_json()
#     user_input = data.get("message", "")

#     if not user_input:
#         return jsonify({"error": "No message provided"}), 400

#     response = get_chatbot_response(user_input, history)

#     history += f"\nUser: {user_input}\nAssistant: {response}"

#     return jsonify({"response": response})

# if __name__ == "__main__":
#     app.run(debug=True)
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  
from app import get_chatbot_response

app = Flask(__name__)
CORS(app)  

history = ""  

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/chat", methods=["POST"])
def chat():
    global history
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = get_chatbot_response(user_input, history)

    history += f"\nUser: {user_input}\nAssistant: {response}"

    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port, debug=True)
