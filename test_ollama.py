import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
        "role":"user",
        "content":"Hello!Introduce yourself."
        }
    ]
)
print(response["message"]["content"])