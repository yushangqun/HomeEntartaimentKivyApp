
import kivy

kivy.require('1.9.1') # the kivy version required



# import the kivy modules/widgets

from kivy.app import App

from kivy.uix.widget import Widget

from kivy.uix.gridlayout import GridLayout

from kivy.uix.videoplayer import VideoPlayer



# An App running a video file

class MyVideoApp(App):
    
    def build(self):
        
        self.player = VideoPlayer(source='/users/shangqunyu/Downloads/videoplayback.mp4', state='stop', options={'allow_stretch': True})
            
        return self.player



# Start the Video App

if __name__ == '__main__':
    
    MyVideoApp().run()
