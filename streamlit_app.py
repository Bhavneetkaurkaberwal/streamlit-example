# faq_bot_streamlit.py
import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Sample FAQ Data
faq_data = {
    "What is your name?": "I'm a FAQ chatbot built with Streamlit.",
    "How do you work?": "I match your questions with the best answer from my FAQ database.",
    "Who created you?": "I was created using OpenAI's GPT and demonstrated with Streamlit."
}

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # Lightweight model for paraphrase detection

def get_answer(question):
    max_similarity = -1
    most_similar_question = ""

    question_embedding = model.encode(question, convert_to_tensor=True)

    for faq_question in faq_data:
        faq_embedding = model.encode(faq_question, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(question_embedding, faq_embedding)

        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_question = faq_question

    # if the similarity is very low, then give a default response
    if max_similarity < 0.5:
        return "Sorry, I don't have an answer to that."
    return faq_data[most_similar_question]

st.title("Paraphrase-aware FAQ Chatbot with Streamlit")

# This uses session state to keep chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Using a key for the text input helps in resetting its value
user_input = st.text_input("You:", key="user_input_key")

if user_input:
    answer = get_answer(user_input)
    
    # Append user's question and bot's answer to chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))
    
    # Clear the input field by setting its value to an empty string
    # st.session_state.user_input_key = ""  

# Display chat history
for role, text in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**{role}:** {text}")
    else:
        st.markdown(f"{role}: {text}")
