from flask import Flask, request, jsonify, render_template

from math_tutor_bot import answer_question
from db import init_db, save_question
from email_utils import send_question_email

app = Flask(__name__)

# Initialize the database table on startup
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    question = (data.get("question") or "").strip()

    if not question:
        return jsonify({"error": "Please provide a question."}), 400

    # 1) store the question
    save_question(question)

    # 2) email ONLY the question
    send_question_email(question)

    # 3) return the bot answer to the user as usual
    answer = answer_question(question)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
