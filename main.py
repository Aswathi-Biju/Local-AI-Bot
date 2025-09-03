import ollama

def chat_with_gpt(prompt):
    response = ollama.chat(
        model="llama3",  
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
