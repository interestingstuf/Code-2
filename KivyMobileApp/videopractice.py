from kivy.app import App
from kivy.uix.video import Video
import os 
import ffmpeg
os.environ["KIVY_VIDEO"]="ffpyplayer"

class Mainapp(App):
    def build(self):
        v1=Video(source="/Users/parthamradkar/Desktop/j.mp4",play=True)
        
        
        return v1

Mainapp().run()        