import speech_recognition as sr
import pyaudio
import pyttsx3
import google.generativeai as genai
from secreatkey import gemini_ai_api_key
from speechregnition import *
from conversation_memory import conversation_memory
#import streamlit as st

#genai.configure(api_key=gemini_ai_api_key)


if __name__ == "__main__":
    print("\n\tWelcome to the Voice Chatbot \t\n")
    print(60*"-")
    print("""Instruction \n
    Start - say hello!..
    End - Say thanks/thankyou!..\n""")
    print(60*"-")
    
    #conversation_memory = []
    count = 0
    
    while True:
        text = speech_to_text()
        print("\t\t\t...AI 🤖")
        try:
            
            if any(i in text for i in ["thank","thanks","thankyou"]):
                conversation_memory.clear()
                text_to_speech("You're welcome! Have a great day!")
                break

            elif text.lower() == "hello":
                text_to_speech("Hi,I am Q and A chatbot, how can I help you?")
            else:
                reply = get_gemini_response(text)
            #final_reply = clean_text(reply)
                text_to_speech(reply)
        except:
            text_to_speech("Sorry I can't Understand it can you tell again loudly")
            count = count + 1
            if count == 2 :
                text_to_speech("Sorry and Thank you! Have a great day!")
                break
