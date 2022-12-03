from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.switch import Switch
from kivy.uix.switch import Switch
class Mainapp(App):
    def function1(self,x):
        print("Succesfully Submitted Form")
    def function2(self,checkbox,value):
        if value:
            print("Box Ticked")
        else:
            print("Box Unticked")    
    def build(self):
        main_layout=BoxLayout(orientation="vertical")
        
        label1=Label(text="View the Image Below. Write What You Notice About The Image. Rate How The Quiz Was", size_hint=(.5,.1), pos_hint={"center_x":.5,"center_y":.5},font_size=40,color=[255/255,21/255,15/255,0.87])
        main_layout.add_widget(label1)
        img=Image(source="/Users/parthamradkar/Desktop/super.png",size_hint=(.5,0.5),pos_hint={"center_x":0.5,"center_y":0.5})
        main_layout.add_widget(img)
        input1=TextInput(size_hint=(.5,.1), pos_hint={"center_x":.5,"center_y":.5},font_size=40,multiline=True,readonly=False)
        main_layout.add_widget(input1)
        cb=CheckBox(active=True)
        cb.bind(active=self.function2)
        main_layout.add_widget(cb)
        pb1=ProgressBar(max=100)
        pb1.value = 20
        main_layout.add_widget(pb1)
        sw1=Switch(active=True)
        main_layout.add_widget(sw1)
        tb1=ToggleButton(text="play",border=(2,2,2,2),font_size=100)
        main_layout.add_widget(tb1)
        button=Button(size_hint=(.5,.1),text="Submit",pos_hint={"center_x":.5,"center_y":.5})
        button.bind(on_press=self.function1)
        main_layout.add_widget(button)
        s1=Slider(orientation="horizontal", value_track=True, value_track_color=(1,0,0,1))
        main_layout.add_widget(s1)
        return main_layout
Mainapp().run()