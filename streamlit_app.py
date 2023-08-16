import streamlit as st

# Sample FAQ Data (You can expand this or use a more advanced data source)
faq_data = {
    "What is your name?": "I'm a FAQ chatbot built with Streamlit.",
    "How do you work?": "I match your questions with the best answer from my FAQ database.",
    "Who created you?": "I was created using OpenAI's GPT and demonstrated with Streamlit."
}

def get_answer(question):
    # Get the closest match to the question from the FAQ data
    # For a real application, you'd likely use a more advanced method, like cosine similarity or a machine learning model
    return faq_data.get(question, "Sorry, I don't have an answer to that.")

st.title("Simple FAQ Chatbot with Streamlit")

user_input = st.text_input("Ask a question:")

if user_input:
    answer = get_answer(user_input)
    st.write(answer)
