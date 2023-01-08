from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name1=ObjectProperty(None)
    email1=ObjectProperty(None)
    def btn(self):
        print("Name:",self.name1.text,"Email: ",self.email1.text)
        self.name1.text=" "
        self.email1.text=" "
class newfile2(App):
    def build(self):
        return MyGrid()

newfile2().run()

