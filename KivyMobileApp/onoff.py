from kivy.app import App
from kivy.uix.switch import Switch

class Mainapp(App):
    def build(self):
        sw1=Switch(active=True)
        
        
        return sw1

Mainapp().run()        