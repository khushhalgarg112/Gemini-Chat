from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

# function to lead gemini pro model
model = genai.GenerativeModel("gemini-pro")
def gemini_res(ques):
    res = model.generate_content(ques)
    return res.text


# Initialize Streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("GEMINI LLM  Application")

input = st.text_input("Input", key="input")
submit = st.button("Ask the Question")

# Opertion after submitting the button

if submit:
    res = gemini_res(input)
    st.subheader("Answer is")
    st.write(res)