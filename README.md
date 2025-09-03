# Local-AI-Bot
# Local AI Chatbot (Python + Ollama)

A simple chatbot built in Python that runs **completely offline** using [Ollama](https://ollama.ai) and open-source LLMs (like LLaMA 3, Mistral, or Gemma).  
This project was originally built with the OpenAI API, but has been adapted to work **100% locally** with no API key or costs. ✅

---

## 🚀 Features
- Chat with AI offline (no internet needed after first model download)
- Easy to set up and run
- Supports multiple models (`llama3`, `mistral`, `gemma`, etc.)
- Exit the chat anytime with `quit`, `exit`, or `bye`

---

## 📂 Project Structure
project1/

│── main.py # Chatbot source code

│── README.md # Documentation


---

## 📦 Installation

### 1. Install Python
Make sure you have **Python 3.9+** installed.  
Check version:
```powershell
python --version
```
If not installed, download from 👉 https://www.python.org/downloads/

---

2. Install Ollama

Download Ollama from 👉 https://ollama.ai

Follow the setup for Windows.

---

3. Pull a Model

Run one of these in PowerShell:
```ollama run llama3```
(or use ollama run mistral for a lighter model)

The model will download once and then run locally.

---

4. Install Python Dependencies

In your project folder, run:
```pip install ollama```

---
▶️ Usage

Run the chatbot:

```python main.py```


Example:

You: Hello
Chatbot: Hi there! How can I help you today?


Exit with:

You: quit

🛠️ Code (main.py)
```
import ollama

def chat_with_gpt(prompt):
    response = ollama.chat(
        model="llama3",  # you can change to "mistral" or "gemma"
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        reply = chat_with_gpt(user_input)
        print("Chatbot:", reply)
```
📌 Notes

First run may take longer (model download).

Models can be 2–8 GB+ depending on choice.

Works fully offline after model is installed.

If you want better performance, try lighter models like Mistral.

📜 License

MIT License

---

⚡ Do you want me to also create a **`requirements.txt`** file for this project, so you (or anyone else) can set it up with one command (`pip install -r requirements.txt`)?
