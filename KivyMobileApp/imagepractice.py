from kivy.app import App
from kivy.uix.image import Image

class Mainapp(App):
   
    def build(self):
        img=Image(source="/Users/parthamradkar/Desktop/super.png",size_hint=(.5,0.5),pos_hint={"center_x":0.5,"center_y":0.5})
        return img
        
    


        
Mainapp().run()
