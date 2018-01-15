from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase

LabelBase.register(name="PTSans", fn_regular="font/PTC55F.ttf")
LabelBase.register(name="PTSansBold", fn_regular="font/PTS76F.ttf")
LabelBase.register(name="PTSansThin", fn_regular="font/PTS55F.ttf")


class CustomFloatLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(CustomFloatLayout, self).__init__(**kwargs)


    def callback(self):
        Factory.ProductPopup().open()
    def callback2(self):
        Factory.TrailerPopup().open()
    def scrollDown(self):
        self.ids["frontScrollView"].scroll_to( self.ids["myVideoPlayer"])


#function for ThumbNailWidget. 
class ProductThumbNailWidget(Widget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            Factory.ProductPopup().open()



class homeEntertaimentApp(App):

    def build(self):
        #from the sake of proper displaying on my laptop, needed to delete for mobile device
        Window.size = (960, 540)

        return CustomFloatLayout()




homeEntertaimentApp().run()

