from dotenv import load_dotenv

load_dotenv()

import os

import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

# function to lead gemini pro model
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

def gemini_res(ques):
    res = chat.send_message(ques, stream=True)
    return res


st.set_page_config(page_title="Q&A Demo")

st.header("GEMINI LLM  Application")


# Intialize session state for history if it don't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input = st.text_input("Input", key="input")
submit = st.button("Ask the Question")

if submit and input:
    res = gemini_res(input)
    # Add user query and response intot he history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Your Answer")
    for chunk in res:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("History")
for person,text in st.session_state['chat_history']:
    st.write(f"{person}: {text}")
