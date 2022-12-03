from kivy.app import App
from kivy.uix.label import Label

class Mainapp(App):
    def build(self):
        label1=Label(text="Hello", size_hint=(.5,.1), pos_hint={"center_x":.5,"center_y":.5},font_size=40,color=[255/255,21/255,15/255,0.87])
        return label1
Mainapp().run()
