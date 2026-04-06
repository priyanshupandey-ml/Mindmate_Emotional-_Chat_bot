<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1 align="center">🤖 Emotion AI Chatbot</h1>

  <p align="center">
    <b>An AI-powered chatbot that understands emotions and responds like a human companion.</b>
  </p>

  <hr>

  <h2>📌 About the Project</h2>
  <p>
    Hello everyone! 👋 <br><br>
    I am currently exploring the field of <b>Machine Learning</b> and AI models. During my learning journey,
    I came across the <b>Hugging Face Transformers</b> library in Python, which provides access to many
    powerful pre-trained models.
  </p>

  <p>
    Nowadays, many people experience <b>mental stress and work pressure</b>, often because they hesitate to share
    their feelings or may not have someone to talk to. 💭
  </p>

  <p>
    To address this, I decided to build an <b>Emotion AI Chatbot</b> that allows users to freely express their
    thoughts and emotions in a safe and interactive environment.
  </p>

  <hr>

  <h2>🚀 Project Idea</h2>
  <p>
    Initially, I planned to build my own Large Language Model (LLM) from scratch. However, creating such a model
    requires a massive amount of <b>data, computational resources, and time</b>.
  </p>

  <p>
    So instead, I leveraged <b>pre-trained models from Hugging Face</b> and plan to fine-tune them later for
    better personalization and performance.
  </p>

  <hr>

  <h2>🧠 Models Used</h2>

  <h3>1️⃣ Emotion Detection Model</h3>
  <p>
    <b>Model:</b> j-hartmann/emotion-english-distilroberta-base <br>
    <b>Purpose:</b> Detects the emotion from user input text (e.g., happy, sad, angry, etc.)
  </p>

  <h3>2️⃣ Conversational Model</h3>
  <p>
    <b>Model:</b> meta-llama/Llama-3.1-8B-Instruct <br>
    <b>Purpose:</b> Generates human-like responses based on user input and detected emotion
  </p>

  <hr>

  <h2>⚙️ Workflow</h2>

  <ol>
    <li>User enters a message or query 💬</li>
    <li>The message is sent to <b>Model 1</b> for emotion detection</li>
    <li>Emotion is extracted (e.g., sad, happy, stressed)</li>
    <li>A function <code>generate_ai_reply(text, emotion)</code> is called</li>
    <li>This function sends a request to <b>Model 2 (LLaMA)</b></li>
    <li>The model generates a response based on both <b>text + emotion</b></li>
    <li>The response is returned via <code>chat_api</code> in JSON format</li>
    <li>User receives the reply through a simple UI interface</li>
  </ol>

  <hr>

  <h2>🛠️ Key Functions</h2>

  <ul>
    <li><b>generate_ai_reply(text, emotion)</b> → Generates AI response</li>
    <li><b>chat_api</b> → Handles API response and returns JSON output</li>
    <li><b>UI/UX Function</b> → Provides chat interface for user interaction</li>
  </ul>

  <hr>

  <h2>✨ Features</h2>

  <ul>
    <li>Emotion-aware responses 🤍</li>
    <li>Human-like conversation using LLM 🤖</li>
    <li>Safe space for users to express feelings 💬</li>
    <li>Scalable architecture for future improvements ⚡</li>
  </ul>

  <hr>

  <h2>🔮 Future Improvements</h2>

  <ul>
    <li>Fine-tuning models for better personalization</li>
    <li>Performance optimization</li>
    <li>Voice-based interaction 🎤</li>
    <li>Memory-based conversations (context awareness)</li>
    <li>Deployment as a web/mobile app</li>
  </ul>

  <hr>

  <h2>📢 Conclusion</h2>
  <p>
    This project is just the <b>beginning</b> of my journey into AI and conversational systems.
    I will continue improving and adding more features to make this chatbot more helpful and intelligent.
  </p>

  <p align="center">
    ⭐ If you like this project, feel free to give it a star!
  </p>

  <hr>

  <p align="center">
    <b>Thank You 🙌</b>
  </p>

</body>
</html>
