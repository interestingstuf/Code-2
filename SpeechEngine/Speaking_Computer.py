

"""
import speech_recognition as sr
from gtts import gTTS, lang
 
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
        print("Please Speak Again")

    text = recognizer.recognize_google(listening)
    Language = "fr"
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

"""
"""
while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as intext:
        print("Please Speak Now")
        listening = recognizer.listen(intext)
        print("Analyzing...")

    try:
        print("Did You Say"+recognizer.recognize_google(listening) )
        Output = recognizer.recognize_google(listening)
    except:
        print("Please Speak Again")


    text = Output
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
    if text == "admin panel":
        print("Please Enter Password")
        AdminPassIn = int(input("What Is The Admin Password"))
        AdminPass = 1234 
        if AdminPassIn == AdminPass:
            print("Access Granted")
            admininput = input("What Do You Want To Change")
            if admininput == "Change Admin Password":
                changeadminpassword = int(input("Enter The New Admin Password MAKE SURE IT IS NUMBER ONLY"))
                changeadminpassword = AdminPass
           
        else:
            print("Please Try Again") 
"""            

import speech_recognition as sr
from gtts import gTTS, lang
 
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
        print("Please Speak Again")

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
