from kivymd.app import MDApp
from kivymd.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu

#from kivy.app import App
#from kivy.uix.camera import Camera
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.properties import*
from random import randint, random
from functools import partial
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.card import MDCard

class Chip(ToggleButton):
    dc=ListProperty([0,0,0,1])
    def __init__(self,**k):
        super().__init__(**k)

    def call(self,):
        print("a")

        if self.state=='down':
            self.dc=[1,1,1,1]
            self.color:[0,0,0,1]
        else:
            self.color=[1,1,1,1]
            self.dc:[0,0,0,1]


class Plate(MDCard):
    _image=StringProperty('')
    menu=None
    _video_title=StringProperty("#01 Introduction to Kivymd & Toolbar")
    _channel_name=StringProperty("Sk Sahil - 79K views - 1 day ago" )
    _rimage=StringProperty('')
    _time=StringProperty('0:00')
    def on_kv_post(self,obj):pass
        
    def open_menu(self,obj):
        if not self.menu:
            _items=["Save to Watch Later",'Save to playlist','Share','Report']
            menu_items = [
            {
                "text": f" {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in _items
        ]
            self.menu = MDDropdownMenu(
                caller=obj,
                items=menu_items,
                width_mult=4,
            )
        self.menu.open()
    def menu_callback(self, text_item):
        print(text_item)




class MainScreen(Screen):pass



class YouTube(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        return MainScreen()




YouTube().run() 
