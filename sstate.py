import ollama
import streamlit as st

st.title("TechBot: The Sarcastic Tech Expert")

# Initialize session state for messages if not exists
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a sarcastic tech expert. Respond to questions with humor and light sarcasm."}]

# Initialize session state for input if not exists
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Text input field (ensure unique key)
user_input = st.text_input("What do you want to ask?", key="user_input_key")

if user_input:
    # Store input in session state to prevent duplication
    st.session_state.user_input = user_input

    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from Ollama
    response = ollama.chat(
        model="mistral",
        messages=st.session_state.messages
    )

    # Extract AI response
    bot_reply = response.get("message", {}).get("content", "Sorry, I have no response.")

    # Append AI response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display conversation
    for msg in st.session_state.messages:
        if msg["role"] != "system":  # Skip system prompt
            st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")

    # Clear input field after submission
    st.session_state.user_input = ""
