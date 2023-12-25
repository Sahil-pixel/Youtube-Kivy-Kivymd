from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.widget import Widget 
from kivy.clock import Clock
class Brick(Widget):
	pass



class Main(FloatLayout):
	def on_kv_post(self,obj):
		Clock.schedule_once(self.init2,)

	def init2(self,dt):
		L=self.width
		print(L)
		n=10
		l=18
		h=18
		gap=(L-n*l)/(n+1)
		y=self.y
		yf=self.height
		center=(yf-y)/2
		initial_y=center
		ny=10
		ygap=(((yf-initial_y))-ny*h)/(ny+1)

		for j in range(1,ny+1):
			for i in range(1,n+1):
				brick=Brick(size_hint=(None,None),size=(l,h))
				brick.pos=(self.x+i*gap+(i-1)*l,center+j*ygap+(j-1)*h )

				self.add_widget(brick)






class BrickGame(App):
	def build(self):
		return Main() 



BrickGame().run()