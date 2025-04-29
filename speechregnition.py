import speech_recognition as sr
import pyaudio
import pyttsx3
import google.generativeai as genai
from secreatkey import gemini_ai_api_key
from conversation_memory import conversation_memory


genai.configure(api_key=gemini_ai_api_key)

def speech_to_text(): 
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as mic:
         print("User 🧑...")
         recognizer.adjust_for_ambient_noise(mic, duration=0.2)
         audio = recognizer.listen(mic)
    try:
         text = recognizer.recognize_google(audio)
         return text
    except:
         return None
     

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    try:
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except RuntimeError:
        print("Speech engine is already running!")
        

def clean_text(text):
    text = text.split("\n")
    cleaned = [line.strip() for line in text if line.strip() != ""]
    cleaned = [line.replace("*", "").replace("**", "") for line in cleaned]
    final_text = " ".join(cleaned)
    return final_text

def get_gemini_response(user_input):
   
    conversation_memory.append(f"User: {user_input}")

   
    context = "\n".join(conversation_memory[-5:])

    # Add your prompt for simplicity
    prompt = f"Here is the conversation so far:\n{context}\nPlease give me a short and easy-to-understand response."

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    # Store AI reply in memory
    ai_reply = clean_text(response.text)
    conversation_memory.append(f"AI: {ai_reply}")

    return ai_reply



