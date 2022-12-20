from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
import os 
import ffmpeg
os.environ["KIVY_VIDEO"]="ffpyplayer"

class Mainapp(App):
    def build(self):
        v1=VideoPlayer(source="/Users/parthamradkar/Desktop/j.mp4")
        
        
        return v1
        


Mainapp().run()        