import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.title("Bollywood Song Emoji Generator")

input = st.text_input("Generate emoji for:")

system_prompt = """
    You will be provided with a Bollywood song in Hindi or Hinglish, and your task is to translate it into emojis. Do not use any regular text. Do your best with emojis only.
"""

if st.button("Generate") and input:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input},
        ],    
        max_tokens=200
    )
    st.text(response.choices[0].message.content)
