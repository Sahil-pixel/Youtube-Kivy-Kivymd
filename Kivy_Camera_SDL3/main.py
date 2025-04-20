'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    RelativeLayout:
        id:r
        

        Camera:
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            id: camera
            resolution: (640,480)
            size_hint:None,None
            fit_mode:'contain'
            size:r.height,r.width
            play: False
            canvas.before:
                PushMatrix
                Rotate:
                    angle: -90
                    origin:self.center
           
            canvas.after:
                PopMatrix
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        if platform=='android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA,Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_MEDIA_IMAGES])
        return CameraClick()


TestCamera().run()