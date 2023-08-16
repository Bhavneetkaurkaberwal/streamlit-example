import streamlit as st
import openai

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


def main():
    st.title("FAQ Chatbot")
    user_question = st.text_input("Ask a question:")
    
    if user_question:
        try:
            # Call the OpenAI API to generate a response
            response = openai.Completion.create(
                engine="davinci",  # You can also use "text-davinci-003"
                prompt=user_question,
                max_tokens=50
            )
            
            # Display the generated response to the user
            st.text("Chatbot: " + response.choices[0].text.strip())
        except Exception as e:
            st.error("An error occurred: " + str(e))

if __name__ == "__main__":
    main()
