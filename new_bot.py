import streamlit as st
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

# Text-to-speech
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(audio)
    engine.runAndWait()


# Listen to microphone once
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language="en-in")
            st.write(f"**You said:** {command}")
            return command
        except Exception as e:
            st.write("Could not understand. Please say again.")
            return "None"


# Tell the day
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday", 7: "Sunday"
    }
    speak(f"The day is {Day_dict[day]}")
    st.write(f"📅 Day: **{Day_dict[day]}**")


# Tell the time
def tellTime():
    now = datetime.datetime.now()
    t = now.strftime("%H:%M")
    speak(f"The time is {t}")
    st.write(f"⏰ Time: **{t}**")


# Main Streamlit App
st.title("🎙️ JM's Voice assistant")

if st.button("Start Listening"):
    query = takeCommand().lower()

    if "open geeksforgeeks" in query:
        speak("Opening GeeksforGeeks")
        webbrowser.open("https://www.geeksforgeeks.org")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "which day" in query:
        tellDay()

    elif "time" in query:
        tellTime()

    elif "from wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("from wikipedia", "")
        result = wikipedia.summary(query, sentences=3)
        speak(result)
        st.write(result)

    elif "your name" in query:
        speak("I am Bot, your assistant")
        st.write("🤖 My name is JM's Bot!")

    elif "bye" in query:
        speak("Goodbye!")
        st.write("👋 Session ended.")
