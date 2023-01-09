from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    uid=ObjectProperty(None)
    pwd=ObjectProperty(None)
    def login(self):
        
        print("Login Succesful With Credentials: ","User ID:",self.uid.text,"Password:",self.pwd.text)
        self.uid.text=" "
        self.pwd.text=" "
class newfile3(App):
    def build(self):
        return MyGrid()

newfile3().run()        