# pip list
# pyautio, SpeechRecognition, 


import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)

print(r.recognize_google(audio))

import googletrans #pip

translator = googletrans.Translator()

answer = r.recognize_google(audio)
result = translator.translate(answer, dest='en')
print(result)
