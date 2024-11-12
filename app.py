from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

st.title('Job Text Generator')
st.subheader('Outline your career and achievements.')
input_text = st.text_area('Career Outline')

if st.button('Generate Bio', type='primary'):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You will be provided with a career summary. Please write a brief, professional, online bio for this person. Use simple, easy to understand language in first-person. Avoid jargon and common cliches."},
        {
            "role": "user",
            "content": input_text
        }
        ]
    )
    
    response_text = completion.choices[0].message.content
    st.header('Profile Summary')
    st.text(response_text)
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You will be provided with a career summary. Please write a very short, simple, verbal introduction for this person to use themselves in professional situations. Avoid jargon and common cliches."},
        {
            "role": "user",
            "content": input_text
        }
        ]
    )
    
    response_text = completion.choices[0].message.content
    st.header('Introduce Yourself')
    st.text(response_text)
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You will be provided with a career summary. Please use it to write the following sections in a professional CV if applicable; career summary, list of skills and professional achievements."},
        {
            "role": "user",
            "content": input_text
        }
        ]
    )
    
    response_text = completion.choices[0].message.content
    st.header('CV')
    st.text(response_text)