from threading import Thread
from gtts import gTTS
import pygame
from io import BytesIO
import speech_recognition as sr
from PyDictionary import PyDictionary
import time
import pyaudio

def main():


    r = sr.Recognizer()
    m = sr.Microphone()

    with m as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(m, callback, phrase_time_limit=3)


    while True:
        pass

    #stop_listening(wait_for_stop=False)

    #thread = Thread(target=ai_activate)
    #thread.start()
    #thread.join()

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("> " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def ai_activate():
    while True:
        init_rec = sr.Recognizer()
        sr.energy_threshold = 300
        with sr.Microphone() as source:
            audio_data = init_rec.listen_in_background(source)
            try:
                text = str(init_rec.recognize_google(audio_data))

                #Debug
                print(text)

                if text.lower() == "hey daisy" or str(text.lower()).startswith("daisy"):
                    runAsNewThread(speakText("haan devil sir"))
                    ai_listening()
                    break

            except:
                pass

def ai_listening():
    init_rec = sr.Recognizer()
    sr.energy_threshold = 300
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5)
        try:
            text = init_rec.recognize_google(audio_data)

            # Debug
            print(text)

            ai_executeTask(text)
            ai_activate()

        except:
            ai_activate()

def ai_executeTask(command):
    cmd = str(command)

    if cmd.endswith("matlab kya hota hai") or cmd.startswith("what is the meaning of"):
        dictionary = PyDictionary()
        meaning = dictionary.meaning(cmd.split(' ')[0])["Noun"][0]
        runAsNewThread(speakText(cmd.replace("matlab kya hota hai", "") + " ka matlab hota hai " + meaning))

def speakText(text):
    tts = gTTS(text, lang='hi')

    audio = BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)

    pygame.mixer.init()

    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

def runAsNewThread(func, waitForExit=True):
    thread = Thread(target=func)
    thread.start()
    if waitForExit:
        thread.join()

if __name__ == "__main__":
    main()