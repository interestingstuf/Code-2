"""
from gtts import gTTS
import os
text = "Hello My Name Is Parth"
Language = "en"
speak = gTTS (text=text, lang=Language, slow=False)
speak.save("Welcome.mp3")
os.system("mpg321 Welcome.mp3")
"""

"""
from gtts import gTTS, lang
import os
text = input("Enter The Question You Have")
Language = "en"
def Speak1(ans):
    speak = gTTS (text=ans, lang=Language, slow=False)
    speak.save("Answer1.mp3")
    os.system("mpg321 Answer1.mp3")



if text == "Hi There":
    ans = "Hi Parth How Are You, How Can I Asist You"
    Speak1(ans)
"""    

from gtts import gTTS, lang
 
import os
while True:

    text = input("Enter The Question You Have")
    Language = "en"
    def Speak1(quest, ans):
        if text == quest:
            speak = gTTS (text=ans, lang=Language, slow=False)
            speak.save("Answer1.mp3")

            os.system("mpg321 Answer1.mp3")



    Speak1("Hello", "Hi Parth")

    Speak1("How Are You", "I am Fine What About You")

    Speak1("Hey", "Yes I Am Here To Answer Your Questions")

    Speak1("What Is Your Favorite Color", "Blue Is My Faveorite Color")

    Speak1("")

    