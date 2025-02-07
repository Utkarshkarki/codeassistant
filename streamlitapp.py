import ollama
import streamlit as st # Import Streamlit library

st.title("TechBot: The Sarcastic Tech Expert")  # Set title of the web app

# System prompt
system_prompt = "You are a sarcastic tech expert. Respond to questions with humor and light sarcasm."

print("Chat with TechBot (type 'exit' to quit):")

messages = [{"role": "system", "content": system_prompt}]  # Store conversation history

while True:
    user_input =st.text_input("what you want: ",key="user_input")
    if user_input.lower() == "exit":
        break
    
    # Append user input to the conversation history
    messages.append({"role": "user", "content": user_input})

    # Get response from Ollama
    response = ollama.chat(
        model="mistral",
        messages=messages  # Includes chat history
    )
    
    # Extract and print AI response
    bot_reply = response["message"]["content"]
    st.write(f"TechBot: {bot_reply}")
    
    # Save the assistant's response
    messages.append({"role": "assistant", "content": bot_reply})
