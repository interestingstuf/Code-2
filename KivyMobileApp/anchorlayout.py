from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


class Mainapp(App):
    def build(self):
        layout=AnchorLayout(anchor_x="center",anchor_y="center")
        b2=Button(text="Hello",size_hint=(.5,.1))
        layout.add_widget(b2)
        return layout
Mainapp().run()