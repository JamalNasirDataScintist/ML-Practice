import os

import streamlit as st
from groq import Groq
import speech_recognition as sr

st.title("Groq Mini Chatbot")
client=Groq(api_key=os.getenv("GROQ_API_KEY"))


def take_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        
        try:
            text=recognizer.recognize_google(audio)
            st.success("You said: " + text)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I did not get that")
            return ""
        except sr.RequestError:
            st.error("Sorry, my speech service is down")
            return ""
        
def ask_groq(prompt):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
            )
        st.write("Groq mini says: ", response.choices[0].message.content)

text_query=st.text_input("Type your question here:")
if text_query:
    prompt=ask_groq(text_query)
    st.markdown("**Groq mini says:**")
    st.write(prompt)
    
if st.button("Speak"):
    voice_input=take_voice_input()
    if voice_input and voice_input.strip():
        prompt=ask_groq(voice_input)
        st.markdown("**Groq mini says:**")
        st.write(prompt)
    