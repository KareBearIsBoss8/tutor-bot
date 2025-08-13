#To generate syllabus_embeddings.json file run below --
#pip install openai tiktoken numpy
#python build_embeddings.py

import json
import os
import numpy as np
from openai import OpenAI
import tiktoken

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the structured syllabus
with open("syllabus_structure.json", "r", encoding="utf-8") as f:
    syllabus = json.load(f)

# Create embeddings
def get_embedding(text, model="text-embedding-3-small"):
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return response.data[0].embedding

embeddings = []
for title, content in syllabus.items():
    text = f"{title}\n{content}"
    embedding = get_embedding(text)
    embeddings.append({
        "title": title,
        "content": content,
        "embedding": embedding
    })

# Save embeddings to a file
with open("syllabus_embeddings.json", "w", encoding="utf-8") as f:
    json.dump(embeddings, f)