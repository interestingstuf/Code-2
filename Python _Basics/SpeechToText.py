import speech_recognition as sr
import time
import sys
recognizer = sr.Recognizer()

with sr.Microphone() as input:
    print("Please Speak Now")
    listening = recognizer.listen(input)

try:

    done = 'false'
    #here is the animation
    def animate():
        while done == 'false':
            sys.stdout.write('\rloading |')
            time.sleep(0.1)
            sys.stdout.write('\rloading /')
            time.sleep(0.1)
            sys.stdout.write('\rloading -')
            time.sleep(0.1)
            sys.stdout.write('\rloading \\')
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

    animate()
    #long process here
    done = 'false'
    print("Did You Say "+recognizer.recognize_google(listening) )

except:
    print("Please Speak Again")