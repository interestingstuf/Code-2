from kivy.app import App
from kivy.uix.textinput import TextInput

class Mainapp(App):
    def build(self):
        input1=TextInput(size_hint=(.5,.1), pos_hint={"center_x":.5,"center_y":.5},font_size=40,multiline=True,readonly=False)
        return input1
Mainapp().run()
