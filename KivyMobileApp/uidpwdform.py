from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    uid=ObjectProperty(None)
    pwd=ObjectProperty(None)
    def login(self):
        uid1=self.uid.text
        pwd1=self.pwd.text
        if uid1 == "Parth" and pwd1 == "1892601":
            #print("Login Succesful With Credentials: ","User ID:",self.uid.text,"Password:",self.pwd.text)
            print("Login Succesful With Given Credentials")
            self.uid.text=" "
            self.pwd.text=" "
        else:
            print("Login Credetials Rejected")    
class newfile3(App):
    def build(self):
        return MyGrid()

newfile3().run()        