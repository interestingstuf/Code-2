import pyttsx3
def say(text,speed):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate',150)