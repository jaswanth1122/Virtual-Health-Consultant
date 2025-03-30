import streamlit as st
import requests
import speech_recognition as sr

st.title("🤖 AI-Powered Virtual Health Consultant")
st.write("Enter your symptoms below to get health advice.")

# Function to recognize voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"Recognized Speech: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError:
        st.error("Speech recognition service unavailable.")
        return ""

# User input for symptoms
symptoms = st.text_area("Describe your symptoms:")

if st.button("🎤 Speak Symptoms"):
    spoken_text = recognize_speech()
    if spoken_text:
        symptoms = spoken_text

if st.button("Analyze"):
    if symptoms.strip():
        response = requests.post("http://127.0.0.1:5000/analyze", json={"symptoms": symptoms})
        if response.status_code == 200:
            st.success(response.json()["result"])
        else:
            st.error("Error processing request. Please try again.")
    else:
        st.warning("Please enter some symptoms.")

# Drug Interaction Checker
st.subheader("💊 Drug Interaction Checker")
medicine_name = st.text_input("Enter Medicine Name:")

if st.button("Check Interaction"):
    if medicine_name.strip():
        response = requests.post("http://127.0.0.1:5000/check_drug", json={"medicine": medicine_name})
        if response.status_code == 200:
            st.success(response.json()["result"])
        else:
            st.error("Error processing request. Please try again.")
    else:
        st.warning("Please enter a medicine name.")