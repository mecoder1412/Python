import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()

def wait_for_enter():
    input("\nPress Enter to stop recording...\n")
    stop_event.set()
# 4. FUNCTION spinner():
#    - While stop_event is not set:
#      - Print rotating spinner in console
#      - Sleep briefly
#    - Once stopped, print "Recording stopped.
def spinner():
    spinner_chars = '|/-\\'
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write('\rRecording... ' + spinner_chars[idx % len(spinner_chars)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write('\rRecording stopped.          \n')
# 5. FUNCTION record_until_enter():
#    - Initialize PyAudio
#    - Open an input stream with format=paInt16, rate=16kHz, channels=1
def record_until_enter():
    p=pyaudio.PyAudio()
    format=pyaudio.paInt16
    channels=1
    rate=16000
    frames_per_buffer=1024
    stream=p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=frames_per_buffer)
    frames=[]
    threading.Thread(target=wait_for_enter).start()
    threading.Thread(target=spinner).start()
    while not stop_event.is_set():
        try:
            data=stream.read(frames_per_buffer)
            frames.append(data)
        except Exception as e:
            print("Error reading stream:", e)
            break
        stream.stop_stream()
        stream.close()   
        sample_width=p.get_sample_size(format)
        p.terminate()
        audio_data=b''.join(frames)
        return audio_data, rate, sample_width
#    - Start threads:
#        - wait_for_enter()
#        - spinner()
#    - While stop_event is not set:
#        - Read audio data from stream
#        - Append data to a list of frames
#    - Stop and close stream
#    - Combine frames into a single bytes object
#    - Return (audio_data, rate, sample_width)

# 6. FUNCTION save_audio(data, rate, width, filename="audio.wav"):
#    - Open a wave file in write-binary mode
#    - Set channels=1, setsampwidth=width, setframerate=rate
#    - Write frames (data) to file
#    - Print confirmation
def save_audio(data, rate, width, filename="audio.wav"):
  with wave.open(filename, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(width)
    wf.setframerate(rate)
    wf.writeframes(data)
  print(f"Saved: {filename}")
# 7. FUNCTION transcribe_audio(data, rate, width, filename="transcription.txt"):
#    - Create an sr.Recognizer
#    - Convert raw data to AudioData
#    - Use Google recognizer to get text
#    - Handle errors appropriately
#    - Save result to file, print text
def transcribe_audio(data,rate, width, filename="transcription.txt"):
    r=sr.Recognizer()
    audio=AudioData(data, rate, width)
    try:
        text=r.recognize_google(audio)
    except sr.UnknownValueError:
        text="Could not understand the audio"
    except sr.RequestError as e:
        text=f"API Error: {e}"
    print("Transcription:", text)
    with open(filename, "w") as f:
        f.write(text)
    print(f"Saved: {filename}")        
# 8. FUNCTION show_waveform(data, rate):
#    - Convert data to numpy array of int16
#    - Create a time axis based on sample count and rate
#    - Plot the waveform with matplotlib
#    - Show the plot
def show_waveform(data, rate):
  samples = np.frombuffer(data, dtype=np.int16)
  time_axis = np.linspace(0, len(samples) / rate, num=len(samples))
  plt.plot(time_axis, samples)
  plt.title("Audio Waveform")
  plt.xlabel("Time (s)")
  plt.ylabel("Amplitude")
  plt.tight_layout()
  plt.show()
# 9. FUNCTION main():
#    - Print "Start speaking..." message
#    - Call record_until_enter() to get audio data
#    - save_audio(...) the data
#    - transcribe_audio(...) the data
#    - show_waveform(...) the data
def main():
    print("Start speaking. Press Enter to stop.")
    audio_data, rate, width=record_until_enter()
    save_audio(audio_data, rate, width)
    transcribe_audio(audio_data, rate, width)
    show_waveform(audio_data, rate)
if __name__ == "__main__":
  main()

