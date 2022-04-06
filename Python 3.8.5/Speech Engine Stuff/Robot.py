"""
import subprocess
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import os

    

recognizer = sr.Recognizer()
while True:
    with sr.Microphone() as input:
        print("Please Speak Now")
        listening = recognizer.listen(input)

        print("Analyzing...")

    try:
        print("Did You Say"+recognizer.recognize_google(listening) )

    except:
        print("HI")
            

   
    
    if recognizer.recognize_google(listening) == "open Discord":
        subprocess.check_call(["open", "-a", "Discord"])
        text = "Opening Now..."
        Language = "en"
        speak = gTTS (text=text, lang=Language, slow=False)
        speak.save("Welcome.mp3")
        os.system("mpg321 OOKAYYYYY.mp3")
            
    elif recognizer.recognize_google(listening)  == "go to Youtube":
        webbrowser.open_new_tab("www.youtube.com")
    elif recognizer.recognize_google(listening)  == "open Google":
        subprocess.check_call(["open", "-a", "Google Chrome"])   
        text = "Opening Now..."
        Language = "en"
        speak = gTTS (text=text, lang=Language, slow=False)
        speak.save("Welcome.mp3")
        os.system("mpg321 OOKAYYYYY.mp3")
            
    elif recognizer.recognize_google(listening)  == "turn on some music":
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=3_-a9nVZYjk")
        
     
        text = "Playing Now..."
        Language = "en"
        speak = gTTS (text=text, lang=Language, slow=False)
        speak.save("Welcome.mp3")
        os.system("mpg321 Welcome.mp3")
"""      
          
import subprocess
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import os

    
def RobotCode():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as input:
            print("Please Speak Now")
            listening = recognizer.listen(input)

            print("Analyzing...")

        try:
            print("Did You Say "+recognizer.recognize_google(listening) )

        except:
            RobotCode()
        
        text = recognizer.recognize_google(listening)
        Language = "en"
        def Speak1(quest, ans):
            if text == quest:
                speak = gTTS (text=ans, lang=Language, slow=False)
                speak.save("Answer1.mp3")

                os.system("mpg321 Answer1.mp3")


        
        Speak1("hello", "Hi")

        Speak1("how are you", "I am Fine What About You")

        Speak1("hey", "Yes I Am Here To Answer Your Questions")

        Speak1("what is your favorite color", "Blue Is My Favorite Color")
        Speak1("is Bob a good boy", "Yes He Is")
            

    
        
        if recognizer.recognize_google(listening) == "open Discord":
            subprocess.check_call(["open", "-a", "Discord"])
            text = "Opening Now..."
            Language = "en"
            speak = gTTS (text=text, lang=Language, slow=False)
            speak.save("Welcome.mp3")
            os.system("mpg321 OOKAYYYYY.mp3")
                
        elif recognizer.recognize_google(listening)  == "go to turn":
            webbrowser.open_new_tab("https://www.youtube.com")
        
                
        elif recognizer.recognize_google(listening)  == "open Google":
            subprocess.check_call(["open", "-a", "Google Chrome"])   
            text = "Opening Now..."
            Language = "en"
            speak = gTTS (text=text, lang=Language, slow=False)
            speak.save("Welcome.mp3")
            os.system("mpg321 OOKAYYYYY.mp3")
                
        elif recognizer.recognize_google(listening)  == "turn on some music":
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=3_-a9nVZYjk")
        
            text = "Playing Now..."
            Language = "en"
            speak = gTTS (text=text, lang=Language, slow=False)
            speak.save("Welcome.mp3")
            os.system("mpg321 Welcome.mp3")

RobotCode()        