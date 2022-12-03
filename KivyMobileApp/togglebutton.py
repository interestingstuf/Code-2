from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class Mainapp(App):
    def build(self):
        tb1=ToggleButton(text="play",border=(2,2,2,2),font_size=100)
        
        
        return tb1

Mainapp().run()        