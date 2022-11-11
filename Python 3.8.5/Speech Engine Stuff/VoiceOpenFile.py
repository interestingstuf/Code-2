
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
    
    if quest == "open Excel":
        subprocess.check_call(["open", "-a", "Microsoft Excel"])
    elif quest == "open Terminal":
        subprocess.check_call(["open", "-a", "Terminal"])
    elif quest == "open clock":
        subprocess.check_call(["open", "-a", "Clock"])   
    elif quest == "open weather":
        subprocess.check_call(["open", "-a", "Weather"])  
    elif quest == "open clock":
        subprocess.check_call(["open", "-a", "Clock"])     
    elif quest == "open browser":
        subprocess.check_call(["open", "-a", "Opera GX "])      
    elif quest == "open app":
        subprocess.check_call(["close", "-a", "Clock"])                
    elif quest == "close":
        break
    else:

        print("That App is Not Coded Into This Sytem")
    

    