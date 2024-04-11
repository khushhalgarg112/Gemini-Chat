from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

# function to lead gemini pro model
model = genai.GenerativeModel("gemini-pro-vision")

def gemini_res(input,image):
    if input != "":
        res = model.generate_content([input,image])
    else:
        res = model.generate_content(image)
    return res.text 


st.set_page_config(page_title="Q&A Demo")

st.header("GEMINI LLM  Application")

input = st.text_input("Input", key="input")

uploaded_file = st.file_uploader("Choose a file...", type=["jpg", "jpeg", "png"])
image =""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uplaoded Image..",use_column_width=True)

submit = st.button("Tell About the Image")

if submit:
    res = gemini_res(input,image)
    st.subheader("Your Response is ")
    st.write(res)