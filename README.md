# **Create a python programe for Speech Regonition**

This project is a **basic Speech Recognition System** that takes user voice input and then responds by speaking back the recognized input.

It demonstrates how to capture audio, convert speech to text, and use text-to-speech to provide a spoken response.

## **Step 1:Capture User Voice Input**
Use the microphone to capture the user's voice and convert the spoken words into text using a speech recognition tool

```markdown
Packages : speech_recognition ,Pyaudio 
     Pyaudio - Capture the audio from micro phone
     speech_recognition - Converting audio signal into data
```

   ```python
   import speech_recognition as sr
   import pyaudio

   def speech_to_text(): 
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as mic:
         print("User 🧑...")
         recognizer.adjust_for_ambient_noise(mic, duration=0.2)
         audio = recognizer.listen(mic)
    try:
         text = recognizer.recognize_google(audio) # convert the audio into text
         return text
    except:
         return None
```

## **Step 2: Send Text to Google Gemini AI**
Send the recognized text to Google Gemini AI and receive a generated response based on the user's input

Use conversational memory (a global variable) to store past conversations, allowing the bot to remember previous chats and provide context-aware replies

```markdown
Packages : google.generativeai
```
```python
import google.generativeai as genai

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
```

## **Step 3: Convert Text to Speech**
Take the AI-generated response and convert the text into spoken words using a text-to-speech engine, allowing the bot to reply to the user with a voice output

```markdown
Package :  pyttsx3
 pyttsx3 - Convert text to speech easily
 [Getting Started with Python Text-to-Speech: A Beginner’s Guide to pyttsx3](https://srivastavayushmaan1347.medium.com/getting-started-with-python-text-to-speech-a-beginners-guide-to-pyttsx3-a105f130c420)

```

```python
import pyttsx3

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
```

#### **Project Interface**
The interface allows the user to speak into the microphone, and the system captures and processes the speech, then responds back with synthesized speech

![Project Interface](images\iference.PNG)
