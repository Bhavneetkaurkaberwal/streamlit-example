# faq_bot_streamlit.py
import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Sample FAQ Data
faq_data = {
    "What is the vacation time allowance?": "Our vacation policy provides for two weeks (10 days) of annual vacation that is accrued as per ESA, (accrued at .83 vacations days/month for tenure up to 5 years, or 1.25 vacation days/month for company tenure of more than 5 years. This vacation is administered on a fiscal (Nov 1- Oct 31st) year basis. Note that it is mandatory to take at least ESA minimums (10 or 15 days, depending on company tenure). These days must be taken within the fiscal year, and do not carry over. We are also pleased to provide up to five (5) additional Plum Flex days to be taken during the year. These days are a benefit that do not accrue and expire at the end of the fiscal year. Any unused Plum Flex days are not paid out in the case of your employment ending at Plum. At the discretion of the company, Plum may shut down every year between Dec. 24-Jan. Note that it may be necessary to be 'on call' during these periods in order to provide continuity of support for customers. For different religious holidays, it is possible that these can be shifted upon request to your leader. Or Requests for alternative time must be approved in advance by your leader.",
    "How do I book vacation or leave time?": "Step 1: Check out your vacation tracker dashboard (click 'calendar') to see pre-allotted STAT and Plum Days, as well as your fellow departments booked time off! Step 2: When you've selected your preferred vacation days, be sure to request leave right in slack by typing '/vacation' [followed by enter, enter] using the VT app to submit your vacation request. Step 3: Once your time off has been approved, make sure your full work day is blocked off in your calendar (from 9am - 5pm ET) *Same format as the STAT calendar blocks I send, making it very apparent that you're entire day is blocked off. Step 4: Once you've blocked off your day, be sure to cancel, re-schedule, or decline any meetings that conflict with your OOO. Step 5: On your day off, remember to update your slack status so that your fellow Plummies know not to slack you, unplug, and enjoy your time off! Vacation best practices: Please avoid booking vacation at the same time as your direct team-members, as we'll need to make sure there is coverage available during your time off! Give your leader as much notice as you can when booking vacation, so they can prepare appropriate coverage. The more you can give, the better! Keep in mind that September and October are Plum's busiest months of the year, please be mindful and do not leave all of your vacation days until the last minute. They won't be rolled over, and most importantly, we want you taking breaks, recharging and preventing burnout - so take your vacation!!! Sick days can't be predicted, no worries! Again, let your leader know as soon as you're able to, make sure you update your email OOO/ slack status, log it in VT (see step 2) and then rest/ recover! You can now log sick days after they've taken place, in the case you didn't log in in VT on the date you were",
    "I'm a lonely 30-something with a dog and a cat who loves to paint. What are some of the social Slack channels I should consider joining?": "Try joining these channels: #pets, #crafting-crew, #random, #forcedfun",
    "How do I submit an expense report?": "Expense reports are to be completed within thirty (30) days of incurring the expense. Attach receipts for all expense reports.",
    "What types of expenses are considered for reimbursement?": "Possible reimbursable Items include: Travel expenses, office supplies, general needs, computer hardware, computer software, and entertainment for clients",
    "What is a donut chat and does it involve donuts?": "There is an app for Slack called Donut. On a bi-weekly basis, you will be paired with someone from a different department than your own for a virtual chat. It's up to you if you want to bring donuts or not!",
    "Where can I find tips on how to interact with people with disabilities?": "In CompanyPublic SharePoint -> Resources - Onboarding -> AODA Training -> AODA Training: Customer Service"
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

st.title("Plum Scout")

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
