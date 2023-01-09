from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class MyGrid(Widget):
    uid=ObjectProperty(None)
    pwd=ObjectProperty(None)
    def login(self):
        uid1=self.uid.text
        pwd1=self.pwd.text
        if uid1 == "Parth" and pwd1 == "1234":
            #print("Login Succesful With Credentials: ","User ID:",self.uid.text,"Password:",self.pwd.text)
            #print("Login Succesful With Given Credentials")
            
            popup1=Popup(title="Great! You're Logged In!",size_hint=(None,None),size=(400,400))
            popup1.open()
            self.uid.text=" "
            self.pwd.text=" "
        else:
            #print("Login Credetials Rejected")
            popup2=Popup(title="Try Again",size_hint=(None,None),size=(400,400))
            popup2.open()    
class newfile3(App):
    def build(self):
        return MyGrid()

newfile3().run()        