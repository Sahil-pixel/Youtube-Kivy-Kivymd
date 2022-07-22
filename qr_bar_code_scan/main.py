###Qrcode Barcode Scanner using kivy ,kivymd Python

from kivy.properties import ObjectProperty
from kivy.clock import mainthread
from kivy.utils import platform


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


from camera4kivy import Preview
from PIL import Image


from pyzbar.pyzbar import decode

class ScanScreen(MDScreen):

	def on_kv_post(self,obj):
		self.ids.preview.connect_camera(enable_analyze_pixels = True,default_zoom=0.0)


	@mainthread
	def got_result(self,result):
		self.ids.ti.text=str(result)


class ScanAnalyze(Preview):
	extracted_data=ObjectProperty(None)


	def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
		pimage=Image.frombytes(mode='RGBA',size=image_size,data=pixels)
		list_of_all_barcodes=decode(pimage)
		

		if list_of_all_barcodes:
		    if self.extracted_data:
		        self.extracted_data(list_of_all_barcodes[0])
		    else:
		        print("Not found")




class QRScan(MDApp):
	def build(self):
		if platform =='android':
			from android.permissions import request_permissions, Permission
			request_permissions([Permission.WRITE_EXTERNAL_STORAGE,Permission.CAMERA,Permission.RECORD_AUDIO])
		return  ScanScreen()



if __name__=='__main__':
	QRScan().run()