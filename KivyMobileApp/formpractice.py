from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Mainapp(App):
    def build(self):
       l=GridLayout(cols=2)
       username=TextInput()
       label1=Label(text="Username")

       l.add_widget(label1)
       l.add_widget(username)
       password=TextInput()
       label2=Label(text="Password") 
       l.add_widget(label2)
       l.add_widget(password)
       dob=TextInput()
       label3=Label(text="DOB")
       l.add_widget(label3)
       l.add_widget(dob)
       return l
Mainapp().run()