import speech_recognition as sr


speech = sr.Recognizer()

with sr.Microphone() as source:
    print ('START')
    text= speech.listen(source)
    print ("END")


VCtitle = speech.recognize_google(text)
print(VCtitle)