from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class Mainapp(App):
    def build(init):
        layout1=RelativeLayout()
        b1=Button(text="Hello",size_hint=(.3,.3),pos_hint={"x":0, "y":0})
        b2=Button(text="Hello",size_hint=(.3,.3),pos_hint={"right":1, "y":0})
        b3=Button(text="Hello",size_hint=(.3,.3),pos_hint={"center_x":.5, "center_y":.5})
        b4=Button(text="Hello",size_hint=(.3,.3),pos_hint={"x":0, "top":1})
        b5=Button(text="Hello",size_hint=(.3,.3),pos_hint={"right":1, "top":1})
        layout1.add_widget(b1)
        layout1.add_widget(b2)
        layout1.add_widget(b3)
        layout1.add_widget(b4)
        layout1.add_widget(b5)
        return layout1
Mainapp().run()        

