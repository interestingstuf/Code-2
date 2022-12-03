
import subprocess
import speech
import speech_recognition as sr

import os
import noti
while True:
    

    recognizer = sr.Recognizer()

    with sr.Microphone() as input:
        print("Please Speak Now")
        listening = recognizer.listen(input)
        finished = recognizer.recognize_google(listening)
        print("Analyzing...")
        print("Performing: "+recognizer.recognize_google(listening) )

    
        

    
         
    output = recognizer.recognize_google(listening)
    quest = output
    Language = "en"
    
    if quest == "open Excel":
        subprocess.check_call(["open", "-a", "Microsoft Excel"])
    
    elif quest == "open Terminal":
        subprocess.check_call(["open", "-a", "Terminal"])
        
    elif quest == "open clock":
        noti.notifyuser("opening clock")
        subprocess.check_call(["open", "-a", "Clock"])

    elif quest == "open weather":
        noti.notifyuser("opening weather")
        subprocess.check_call(["open", "-a", "Weather"])

    elif quest == "gaming time":
        noti.notifyuser("opening lunar lets go have gaming time")
        subprocess.check_call(["open", "-a", "Lunar Client"])
    elif quest == "open Roblox":
        noti.notifyuser("opening Roblox")
        subprocess.check_call(["open", "-a", "Roblox"])    
    elif quest == "open app store":
        noti.notifyuser("opening app store")
        subprocess.check_call(["open", "-a", "App Store"])    
                  
    elif quest == "close":
        noti.notifyuser("Program is closing")
        speech.say("Closing","20")
        break
        
    else:

        print("That App is Not Coded Into This Sytem")
    

    