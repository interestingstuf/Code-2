from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class Mainapp(App):
    def build(self):
        pb1=ProgressBar(max=100)
        pb1.value = 20
        
        return pb1

Mainapp().run()        