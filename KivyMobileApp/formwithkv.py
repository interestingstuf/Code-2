from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.label import Label 
#from kivy.uix.button import Button
from kivy.uix.widget import Widget
class MyGrid(Widget):
    pass
class newfile1(App):
    
    def build(self):
        return MyGrid()
    def f1(x):
        print("You Pressed The Button")
newfile1().run()
