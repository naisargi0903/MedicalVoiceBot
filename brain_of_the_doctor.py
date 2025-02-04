import os
import base64
from groq import Groq

# Specific configurations
IMAGE_PATH = "Acne.jpg"
QUERY = "Is there something wrong with my face?"
MODEL = "llama-3.2-90b-vision-preview"

def read_groq_api_key(env_file_path='.env'):
    with open(env_file_path, 'r') as env_file:
        for line in env_file:
            if line.startswith('GROQ_API_KEY='):
                return line.strip().split('=')[1]
    raise ValueError("GROQ_API_KEY not found in .env file")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyse_image_with_query(query=QUERY, model=MODEL, image_path=None):
    GROQ_API_KEY = read_groq_api_key()
    
    # Encode the image if a path is provided
    if image_path:
        encoded_image = encode_image(image_path)
    
    client = Groq(api_key=GROQ_API_KEY)
    
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    
    return chat_completion.choices[0].message.content