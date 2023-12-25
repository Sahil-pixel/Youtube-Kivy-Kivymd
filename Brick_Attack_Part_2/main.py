from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.widget import Widget 
from kivy.clock import Clock
from kivy.properties import BooleanProperty,NumericProperty,ReferenceListProperty,ObjectProperty,ListProperty
from kivy.vector import Vector

class Ball(Widget):
	pass

class Brick(Widget):
	pass



class Main(FloatLayout):
	game_sate=BooleanProperty(True)
	velo_x=NumericProperty(0)
	velo_y=NumericProperty(0)
	velocity=ReferenceListProperty(velo_x,velo_y)
	ball=ObjectProperty(None)
	bricks=[]

	def on_kv_post(self,obj):
		Clock.schedule_once(self.init2,)

	def init2(self,dt):
		fps=60

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
				self.bricks.append(brick)
		self.ball=Ball(size_hint=(None,None))
		self.add_widget(self.ball)
		self.velocity=(1,1)
		Clock.schedule_interval(self.game_loop,1/fps)
		print(self.bricks)
	
	def game_loop(self,dt):
		if self.game_sate:
			self.ball.pos=Vector(*self.velocity)+self.ball.pos
			if self.ball.top>=self.top :
				self.velocity[1]=self.velocity[1]*(-1.5)
			if self.ball.y<=self.y:
				print("Game Over")
				self.game_sate=False
			if self.ball.x<=self.x or self.ball.right>=self.right:
				self.velocity[0]=self.velocity[0]*(-1.5)


			for i in self.bricks:
				if self.ball.collide_widget(i):
					print("Collide")
					self.remove_widget(i)





			print("In Game loop")






class BrickGame(App):
	def build(self):
		return Main() 



BrickGame().run()