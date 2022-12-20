from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class Mainapp(App):
    def build(self):
        f=StackLayout()
        for i in range(20):
            btn=Button(text=str(i),size_hint=(0.05,0.05))
            f.add_widget(btn)

 


  
        
        return f
Mainapp().run()