# pip list
# pyautio, SpeechRecognition, 


import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('dataset_0'+'.wav')
with harvard as source: 
    audio = r.record(source)
text = r.recognize_google(audio, language='ko-KR')
print(text)