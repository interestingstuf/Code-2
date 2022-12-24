from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

class Mainapp(App):
    def build(self):
        layout=AnchorLayout(anchor_x="right",anchor_y="bottom")
        #g=GridLayout(cols=2,row_force_default=True,row_default_height=100)
        g=GridLayout(cols=4)
        b2=Button(text="Hello",size_hint=(None,1),width=80)
        b3=Button(text="Bye",size_hint=(None,1),width=80)
        b4=Button(text="What",size_hint=(None,1),width=80)
        b5=Button(text="Word",size_hint=(None,1),width=80)
        g.add_widget(b2)  
        g.add_widget(b3)
        g.add_widget(b4)
        g.add_widget(b5)  
        layout.add_widget(g)
        return layout
               
       
        
Mainapp().run()