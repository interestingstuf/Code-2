from kivy.app import App
from kivy.uix.checkbox import CheckBox

class Mainapp(App):
   

    def build(self):
        def f1(checkbox,value):
            if value:
                print("The Check Box Is Ticked")
            else:
                print("The Check Box Is Not Ticked")    
        cb=CheckBox()
        cb.bind(active=f1)
    


        return cb

Mainapp().run()
