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
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.storage.jsonstore import JsonStore

#import some fonts
LabelBase.register(name="PTSans", fn_regular="font/PTC55F.ttf")
LabelBase.register(name="PTSansBold", fn_regular="font/PTS76F.ttf")
LabelBase.register(name="PTSansThin", fn_regular="font/PTS55F.ttf")

#load Json File

store = JsonStore('test.json')



class ProductPopup(ModalView):
    pass

class MainView(FloatLayout):

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)

        for x in range (0, store.count()):
            tmpProduct = ProductThumbNailWidget()
            tmpProductId = 'product' + str(x)
            tmpProduct.id = tmpProductId
            tmpProduct.ids.productName.text = store.get(tmpProductId)['name']
            tmpProduct.ids.productImage.source = store.get(tmpProductId)['productImageSource']
            self.ids.product_Display.add_widget(tmpProduct)


        self.ids.product_Display.size_hint_x=0.25 * store.count()

    def callback2(self):
        print("helloworld")
        Factory.TrailerPopup().open()
    def scrollDown(self):
        self.ids["frontScrollView"].scroll_to( self.ids["myVideoPlayer"])


# function for ThumbNailWidget.
class ProductThumbNailWidget(Button):
    def click(button):

        # clear the color for the previous button
        for child in button.parent.children:
            child.background_color = (1,1,1,1)

        # identfy the selected button by put on a different color
        button.background_color = (0,160,66,.9)

        # create a new popup and set context accordingly
        theProductPopup= ProductPopup()
        theProductPopup.ids.productDetailText.text = store.get(button.id)['productDetail']
        theProductPopup.ids.productName.text = store.get(button.id)['name']
        theProductPopup.ids.productImage.source = store.get(button.id)['productImageSource']
        theProductPopup.open()



class ProductDisplayGridLayout(GridLayout):
    pass


class homeEntertaimentApp(App):

    def build(self):
        # for the sake of proper displaying on my laptop, needed to delete for mobile device
        Window.size = (960, 540)

        return MainView()





homeEntertaimentApp().run()

