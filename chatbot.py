import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
st.title("🤖 AI Chatbot")
st.write("Your intelligent AI assistant")
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    response = client.models.generate_content(
    model='gemini-3.5-flash', contents=user_input
 )
    st.write(response.text)