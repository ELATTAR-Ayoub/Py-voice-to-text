# ------------Besmi Allah------------

# First you should install two python packagases
# The first package is SpeechRecognition
# The second package is PyAudio

# SpeechRecognition ---> Allows python to turn your voice to text by contacting the google api
# PyAudio ---> Allows audio to get data from your mic

import speech_recognition as sr
import time

# That's the code to show the list of your device's microphones.

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
# print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name)).


listener = sr.Recognizer()

def voice_to_text():
    try:
        print("A moment of silence, please...")
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(listener.energy_threshold))
        print("Say something...")
        with sr.Microphone() as source:
            Voice = listener.listen(source)
        print("Got it! Recognizing...")
        try:
            # recognize speech using Google Speech Recognition.
            text = listener.recognize_google(Voice)
            #return the voice as a text.
            return text

        # Exception if the programme didn't understand the voice.
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        #Exception if the google server couldn't recognize the voice.
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        time.sleep(0.5)  # sleep for a little bit.
    except KeyboardInterrupt:
        pass

# Now let's do the opposite and turn text to voice.
# pyttsx3 ---> Allows python to turn your text to voice by contacting the google api.

import pyttsx3

engine = pyttsx3.init()

def text_to_voice(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # changing index changes voices.
    engine.say(text)
    engine.runAndWait()

# If you want to change a language you need to change to another "voice" that supports your language.
 # To see which voices/languages are installed you can list them like this:

#for voice in engine.getProperty('voices'):
#   print(voice)


# -------------- The Real Programme ------------------------------------------------------------------------------------

text = voice_to_text()
print(text)
text_to_voice(text)



