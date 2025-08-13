# app.py
from flask import Flask, request, jsonify, render_template
from math_tutor_bot import answer_question
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data.get("question", "")
    if not user_question:
        return jsonify({"error": "❗ Please provide a math 21-127 question."}), 400

    try:
        response = answer_question(user_question)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)