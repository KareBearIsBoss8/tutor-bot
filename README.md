# 🧮 Karolena Math Tutor Bot
 
A friendly, AI-powered tutor bot for Carnegie Mellon's **Math 21-127 (Concepts of Mathematics)** course. 
Built with Flask and OpenAI, the bot answers student questions using the official course syllabus.
 
## 🌐 Live Demo
Once deployed, link your Render web app here: 
👉 [View Live Tutor Bot](https://karolena-math-tutor-bot.onrender.com)
 
---
 
## 📋 Features
- Answers math questions based on a course textbook PDF
- Section-based search: Matches student questions to the most relevant syllabus section using embeddings.
- Uses OpenAI GPT-3.5 for natural language responses
- Web interface with a clean chat UI with HTML, CSS and JavaScript.
- Flask backend: Lightweight Python API for handling requests.
- Fast startup: Pre-computed embeddings stored in syllabus_embeddings.json (no parsing at runtime).
- Supports deployment via Render
 
 
---
 
## 🛠 Tech Stack
 
- Python + Flask
- OpenAI GPT-3.5
- HTML/CSS
- Render (for deployment)
- PyPDF2 + requests
- NumPy
