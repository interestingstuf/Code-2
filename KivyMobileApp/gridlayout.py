from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Mainapp(App):
    def build(self):
        g=GridLayout(cols=3)        
        b=Button(text="Hello")
        g.add_widget(b)
        g.add_widget(Button(text="World"))
        g.add_widget(Button(text="Welcome To"))
        g.add_widget(Button(text="Page"))
        return g
Mainapp().run()