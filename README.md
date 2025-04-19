
#  LLM Chatbot using Flask 🚀

A simple web-based chatbot built using **Flask** and **Python**.  
This project creates an interactive chatbot interface where users can chat with a basic AI model running on a server.

---

## ✨ Features
- Chatbot built with Flask (Python web framework)
- Basic natural language responses
- Frontend developed using simple **HTML templates**
- Backend logic handled in **Python** (`chatbot.py`)
- Lightweight and easy to deploy locally

---

## 🛠 Project Structure
```
flask-chatbot/
├── templates/
│   └── index.html       # Chatbot frontend (HTML)
├── app.py               # Main Flask app to run server
├── chatbot.py           # Simple chatbot response logic
├── requirements.txt     # Python libraries needed
└── README.md            # Project documentation
```

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jagdish0307/flask-chatbot.git
   cd flask-chatbot
   ```

2. **Create Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App**
   ```bash
   python app.py
   ```

5. **Visit in Browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 📋 How It Works
- `app.py` sets up the Flask server and routes user input.
- `chatbot.py` contains the **response generation logic** for the chatbot.
- User input is taken from the HTML form and a response is generated dynamically.

---


## 🔗 Connect with Me
Made with ❤️ by [@jagdish0307](https://github.com/jagdish0307)

