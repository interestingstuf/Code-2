from kivy.app import App
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
#import os 
#import ffmpeg
#os.environ["KIVY_VIDEO"]="ffpyplayer"

class Mainapp(App):
    def build(self):
        v1=SoundLoader.load("/Users/parthamradkar/Documents/music.mp3")
        
        if v1:
            v1.play()
        
        return Label(text="Music Is Playing")

Mainapp().run()        