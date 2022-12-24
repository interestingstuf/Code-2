import os
os.environ["KIVY_VIDEO"]="ffpyplayer" 
from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
import ffmpeg


class Mainapp(App):
    def build(self):
        v1=VideoPlayer(source="j.mp4")
        v1.state="play"
        
        
        
        return v1
        


Mainapp().run()        