
import subprocess

import speech_recognition as sr
 
import os
while True:
    

    recognizer = sr.Recognizer()

    with sr.Microphone() as input:
        print("Please Speak Now")
        listening = recognizer.listen(input)
        print("Analyzing...")

    try:
        print("Did You Say"+recognizer.recognize_google(listening) )

    except:
        print("HI")
         
    output = recognizer.recognize_google(listening)
    quest = output
    Language = "en"
    
    if quest == "Jarvis open Excel":
        subprocess.check_call(["open", "-a", "Microsoft Excel"])
    elif quest == "Jarvis open Discord":
        subprocess.check_call(["open", "-a", "Discord"])
    elif quest == "Jarvis open Google":
        subprocess.check_call(["open", "-a", "Google Chrome"])
    
    else:
        print("That App is Not Coded Into This Sytem")
        break

    