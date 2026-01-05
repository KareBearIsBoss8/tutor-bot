# 🧮 Karolena Math Tutor Bot

An AI-powered tutor bot for **Carnegie Mellon’s Math 21-127 (Concepts of Mathematics)** course.  
Built with Flask and OpenAI, the app helps students ask questions about course material and receive clear, syllabus-grounded explanations, while also allowing the project owner to collect and review submitted questions.

---

## 🌐 Live Demo
👉 [View Live Tutor Bot](https://karolena-math-tutor-bot.onrender.com)

---

## 📋 Overview

Students can submit questions related to Math 21-127 concepts and receive instant AI-generated responses based on the official course syllabus.

In addition to answering questions, the app also:
- Stores every submitted question in a database
- Emails each question to the project owner
- Helps identify common topics students struggle with

This makes the app both a **learning tool for students** and a **feedback tool for instructors or developers**.

---

## ✨ Features

### 🧠 Intelligent Question Answering
- Uses OpenAI’s language models to generate explanations  
- Uses **OpenAI GPT-4-turbo** for natural language responses
- Grounds responses in the official course syllabus  
- Answers math questions based on a **course textbook and syllabus PDF**
- Matches questions to the most relevant syllabus section using precomputed embeddings  

### ⚡ Fast and Lightweight
- Embeddings are generated ahead of time and stored locally  
- Pre-computed embeddings stored in `syllabus_embeddings.json`
- No PDF parsing or embedding generation at runtime  
- Optimized for fast startup on Render  

### 🗄️ Question Tracking
- Every submitted question is saved to a PostgreSQL database  
- Enables future analysis of common topics and misconceptions  

### 📧 Email Notifications
- Each question is emailed to the project owner upon submission  
- Uses SendGrid for reliable email delivery  

### 🌐 Web Interface
- Clean, simple chat-style UI  
- Built with HTML, CSS, and JavaScript  
- Flask backend provides a lightweight Python API for handling requests

---

## 🛠 Tech Stack

### Backend
- **Python + Flask**
- **OpenAI GPT-3.5**
- **PyPDF2**
- **NumPy**
- **requests**

### Database
- **PostgreSQL** (Render managed database)

### Frontend
- **HTML**
- **CSS**
- **JavaScript**

### Infrastructure & Deployment
- **Render** (web hosting and database)

### Data and Utilities
- **Precomputed syllabus embeddings** (`syllabus_embeddings.json`)

---

## 🚀 Deployment

The app is designed for deployment on **Render** using:
- A single Flask web service
- A managed PostgreSQL database
- Environment variables for API keys and email configuration

---

