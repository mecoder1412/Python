import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime
# Load Vosk model (ensure this path exists!)
MODEL_PATH = r"C:\Users\Imani\Documents\python AI\speech recognision\vosk-model-small-en-us-0.15"
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init()
#Callback function
def callback(indicata, frames, time, status):
    if status:
        print("Audio status:", status)
    audio_queue.put(bytes(indicata))
#Query processor
def process_query(query):
    query=query.lower()
    if "time" in query:
        now=datetime.datetime.now().strftime("%H:%M") 
        return f"The current time is {now}."
    elif "date" in query:
        today=datetime.datetime.now().strftime("%B %d, %Y") 
        return f"The current time is {today}." 
    else:
        return "I am sorry, I did not understand that."
# Audio stream
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback):
    print("Listening... Press Ctrl+C to stop.") 
    try:
        while  True:
            data=audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result=json.loads(recognizer.Result()) 
                if "text" in result and result["text"]:
                    query=result["text"]
                    print(f"User:{query}")
                    response=process_query(query
                    )
                    print(f"Assistant: {response}")
                    tts_engine.stop()
                    tts_engine.say(response)
                    tts_engine.runAndWait() 
    except KeyboardInterrupt:
        print("Stopped by user")                      