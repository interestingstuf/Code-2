from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class Mainapp(App):
    def build(self):
        l1=BoxLayout(orientation="horizontal")
        l2=BoxLayout(orientation="horizontal")
        b1=Button(text="Click 1")
        b2=Button(text ="Click 2")
        l2.add_widget(b1)
        l2.add_widget(b2)
        l3=BoxLayout(orientation="vertical")
        b3=Button(text="Click 3")
        b4=Button(text="Click 4")
        l3.add_widget(b3)
        l3.add_widget(b4)
        l1.add_widget(l2)
        l1.add_widget(l3)
        return l1
      
       
        
Mainapp().run()