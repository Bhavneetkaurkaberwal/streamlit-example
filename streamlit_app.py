import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


class FAQChatbot:
    def __init__(self):
        self.faq_database = {
            "What is ChatGPT Mini?": "ChatGPT Mini is a smaller version of the ChatGPT model designed for quick responses.",
            "How much does ChatGPT Mini cost?": "ChatGPT Mini is available for free for limited usage. For extended usage, please refer to our pricing page.",
            "How can I integrate ChatGPT Mini into my website?": "You can integrate ChatGPT Mini using our provided APIs. Documentation is available on our official website.",
            "Is there customer support for ChatGPT Mini?": "Yes, we offer 24/7 customer support for ChatGPT Mini subscribers.",
            "Is my data safe with ChatGPT Mini?": "Yes, we prioritize user data privacy and do not store any personal data from user queries."
        }

    def get_response(self, query):
        response = self.faq_database.get(query, "Sorry, I don't have an answer for that. Please check our official website or contact support.")
        return response

    def demo(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Chatbot: Goodbye!")
                break
            response = self.get_response(user_input)
            print("Chatbot:", response)


# Let's demo the chatbot
if __name__ == "__main__":
    bot = FAQChatbot()
    print("ChatGPT Mini FAQ Chatbot! Type 'exit' to quit.")
    bot.demo()
