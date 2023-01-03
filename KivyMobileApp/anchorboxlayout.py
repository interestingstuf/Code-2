from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

class Mainapp(App):
    def build(self):
        layout1=AnchorLayout(anchor_x="left",anchor_y="bottom")
        b2=Button(text="Hello",size_hint=(.3,.3))
        layout1.add_widget(b2)
        layout2=AnchorLayout(anchor_x="right",anchor_y="top")
        b3=Button(text="Bye",size_hint=(.3,.3))
        layout2.add_widget(b3)
        

       
        g=BoxLayout()
        
       
        g.add_widget(layout1)  
        g.add_widget(layout2)
      
       
        return g
               
       
        
Mainapp().run()