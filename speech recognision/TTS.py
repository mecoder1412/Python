import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator #Google Translate API

#initialize text-to-speech engine
def speak(text, language="en"):
    engine=pyttsx3.init()
    engine.setProperty('rate', 150)#Speed of speech
    voices=engine.getProperty('voices')
    #set for English or other language if supported by pyttsx3
    if language=="en":
        engine.setProperty('voice', voices[0].id)#Default English voice
    else:
        engine.setProperty('voice', voices[1].id)#Other English voice
    engine.say(text)
    engine.runAndWait()
#Speech-to-text: recognize spoken language (english)
def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("????? Please speak now in English") 
        audio=recognizer.listen(source) 
    try:
        print("???? Recognizing speech....")
        text=recognizer.recognize_google(audio,language="en-US")#Use English for speech recognition
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""
def translate_text(text, src_language="en", dest_language="es"):
  try:
    translated = GoogleTranslator(source=src_language, target=dest_language).translate(text)
    print(f"Translated ({dest_language}): {translated}")
    return translated
  except Exception as e:
    print(f"Translation error: {e}")
    return None  
# Main Program
if __name__ == "__main__":
  # Step 1: Recognize speech in source language
  source_language = "en" # English
  text = speech_to_text()
  if text:
    # Step 2: Translate to target language
    target_language = "es" # Spanish
    translated_text = translate_text(text, src_language=source_language, dest_language=target_language)
    if translated_text:
      # Step 3: Speak the translated text
       speak(translated_text)    
 