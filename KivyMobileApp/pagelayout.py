from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

class Mainapp(App):
    def build(self):
        f=PageLayout()
        f.add_widget(Button(text="Hello",background_color=(1,.8,.9,1)))
        f.add_widget(Button(text="World",background_color=(9,.6,.2,1)))
        f.add_widget(Button(text="Bye",background_color=(2,.45,.40,1.45)))

 


  
        
        return f
Mainapp().run()