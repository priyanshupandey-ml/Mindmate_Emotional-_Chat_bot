import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables FIRST, before other imports
load_dotenv()

from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# NEW IMPORT FOR HUGGING FACE CHAT API
from huggingface_hub import InferenceClient
import requests
import json


# ---------------------------------------------------
#   EMOTION DETECTION MODEL
# ---------------------------------------------------

tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

labels = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]

def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    top_idx = torch.argmax(probs, dim=1).item()
    return labels[top_idx]


# ---------------------------------------------------
#   HUGGING FACE CHAT MODEL
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

HF_API_TOKEN = os.getenv("API_KEY")
MODEL = "meta-llama/Llama-3.1-8B-Instruct"

def generate_ai_reply(user_message, emotion):

    system_prompt = f"""
You are an empathetic, human-like emotional support chatbot.
Understand and respond deeply based on the user's emotion: {emotion}.
Your tone should  be soft, caring, warm, and comforting not always in same tone adjust according to user question.
Along with emotional support, gently suggest psychological techniques appropriate to their condition, such as meditation, grounding methods, deep-breathing exercises, journaling, mindfulness, reframing thoughts, or relaxation techniques — but only when helpful and never forcefully.
Avoid sounding robotic; keep your responses natural, safe, and human-like.
Respond in 2–4 short lines.Depending on the user's emotional state, adapt your suggestions accordingly.
Your purpose is to make the user feel heard, understood, and supported.
"""

    url = "https://router.huggingface.co/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 180,
        "temperature": 0.8
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return f"API Error: {response.text}"

    resp_json = response.json()

    return resp_json["choices"][0]["message"]["content"]


# ---------------------------------------------------
#   DJANGO VIEWS
# ---------------------------------------------------

def chat_view(request):
    return render(request, "index.html")


@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "").lower()
        emotion = classify_text(user_message)

        # Generate reply using Hugging Face LLM
        reply = generate_ai_reply(user_message, emotion)

        return JsonResponse({
            "reply": reply,
            "emotion": emotion
        })

    return JsonResponse({"error": "Invalid request"}, status=400)
