from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Mainapp(App):
    def build(self):
       l=GridLayout(cols=2)
       brightnesscontrol=Slider(min=0,max=100)
       label1=Label(text="Brightness")

       l.add_widget(label1)
       l.add_widget(brightnesscontrol)
       soundcontrol=Slider(min=0,max=100)
       label2=Label(text="Sound") 
       l.add_widget(label2)
       l.add_widget(soundcontrol)
       alarmsoundcontrol=Slider(min=0,max=100)
       label3=Label(text="Alarm Volume")
       l.add_widget(label3)
       l.add_widget(alarmsoundcontrol)
       return l
Mainapp().run()