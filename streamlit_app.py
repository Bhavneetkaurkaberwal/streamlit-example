import streamlit as st

# Sample FAQ Data (You can expand this or use a more advanced data source)
faq_data = {
    "What is your name?": "I'm a FAQ chatbot built with Streamlit.",
    "How do you work?": "I match your questions with the best answer from my FAQ database.",
    "Who created you?": "I was created using OpenAI's GPT and demonstrated with Streamlit."
}

def get_answer(question):
    return faq_data.get(question, "Sorry, I don't have an answer to that.")

st.title("Conversation-style FAQ Chatbot with Streamlit")

# This uses session state to keep chat history
# Check if 'chat_history' is already in the session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    answer = get_answer(user_input)
    
    # Append user's question and bot's answer to chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))
    
    st.session_state.user_input_key = ""    # Clear the input field by setting its value to an empty string

# Display chat history
for role, text in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**{role}:** {text}")
    else:
        st.markdown(f"{role}: {text}")
