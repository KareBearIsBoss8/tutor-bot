# math_tutor_bot.py

import json
import numpy as np
import os
from openai import OpenAI
from numpy.linalg import norm

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load syllabus structure and embeddings
with open("syllabus_structure.json", "r") as f:
    section_data = json.load(f)

with open("syllabus_embeddings.json", "r") as f:
    embeddings_data = json.load(f)

# Compute cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))

# Find the best matching section above a confidence threshold
def find_best_section(user_question, threshold=0.55):
    question_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_question
    ).data[0].embedding

    best_section = None
    best_score = -1

    for item in embeddings_data:
        section_title = item["title"]
        section_embedding = np.array(item["embedding"])
        score = cosine_similarity(question_embedding, section_embedding)
        if score > best_score:
            best_score = score
            best_section = section_title

   #print(f"Best match: {best_section} (Score: {best_score:.4f})")    

    return best_section if best_score >= threshold else None

# Generate an answer using the most relevant section
def answer_question(user_question):
    section_title = find_best_section(user_question)

    if section_title:
        section_content = section_data.get(section_title, "")
        prompt = f"""
You are a helpful and patient math tutor for Math 21-127 (Concepts of Mathematics).
Use the following section from the syllabus to answer the question.

📘 Section: {section_title}
{section_content}

Student Question: {user_question}
"""
    else:
        prompt = f"""
You are a helpful and patient math tutor for Math 21-127 (Concepts of Mathematics).
Based on your knowledge, choose the best answer for this student's question.

Student Question: {user_question}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    if section_title:
        return f"📘 **Relevant Section**: {section_title}\n\n{response.choices[0].message.content}"
    else:
        return f"{response.choices[0].message.content}"