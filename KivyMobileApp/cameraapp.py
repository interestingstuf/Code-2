from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import os 
import ffmpeg
os.environ["KIVY_GL_BACKEND"]="gl"
import kivy
class Mainapp(App):
    def onclick(self,*args):
        self.camera.export_to_png("/Users/parthamradkar/Desktop/photo/abc.png")
        print("Taken")

    def build(self):
        layout=BoxLayout(orientation="vertical")
        self.camera= Camera(play=True)
        self.camera.play=True
        self.camera.resolution=(300,300)
        self.click=Button(text="Take photo",size_hint=(.5,.2),pos_hint={"x":.25,"y":.75})
        self.click.bind(on_press=self.onclick)
        layout.add_widget(self.camera)
        layout.add_widget(self.click)
        return layout


Mainapp().run()        