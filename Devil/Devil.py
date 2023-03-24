import speech_recognition as sr
import time
import pyaudio

while True:
    time.sleep(2)
    init_rec = sr.Recognizer()
    sr.energy_threshold = 300
    
    print("Let's speak!!")
    
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5)
        print("Recognizing your text.............")
        try:
            text = init_rec.recognize_google(audio_data)
            print(text)
        except:
            print("Nothing recognized !")
        