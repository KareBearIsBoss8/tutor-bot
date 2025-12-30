from flask import Flask, request, jsonify, render_template
from concurrent.futures import ThreadPoolExecutor

from math_tutor_bot import answer_question
from db import init_db, save_question
from email_utils import send_question_email

app = Flask(__name__)
init_db()

# Small thread pool for post-response work
executor = ThreadPoolExecutor(max_workers=2)

def _postprocess(question: str):
    # Save + email in background; log failures so you can debug
    try:
        save_question(question)
        app.logger.info("Saved question to DB")
    except Exception:
        app.logger.exception("DB save failed")

    try:
        send_question_email(question)
        app.logger.info("Email send queued")
    except Exception:
        app.logger.exception("Email send failed")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Please provide a question."}), 400

    # 1) Compute answer first (what user cares about)
    answer = answer_question(question)

    # 2) Kick off save + email AFTER answer is ready
    executor.submit(_postprocess, question)

    # 3) Respond immediately
    return jsonify({"answer": answer})
