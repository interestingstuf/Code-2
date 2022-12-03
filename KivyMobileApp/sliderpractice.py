from kivy.app import App
from kivy.uix.slider import Slider

class Mainapp(App):
    def build(self):
        s1=Slider(orientation="horizontal", value_track=True, value_track_color=(1,0,0,1))
        return s1

Mainapp().run()        