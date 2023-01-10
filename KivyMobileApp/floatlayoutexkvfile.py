from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    Name=ObjectProperty(None)
    Password=ObjectProperty(None)
    
class newfile4(App):
    def build(self):
        return MyGrid()

newfile4().run()        