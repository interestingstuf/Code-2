from kivy.app import App
from kivy.uix.button import Button

class Mainapp(App):
    def function1(self,x):
        print("You clicked the button")
    def build(self):
        button=Button(size_hint=(.5,.1),text="Click Me",pos_hint={"center_x":.5,"center_y":.5})
        button.bind(on_press=self.function1)
    


        return button

Mainapp().run()
