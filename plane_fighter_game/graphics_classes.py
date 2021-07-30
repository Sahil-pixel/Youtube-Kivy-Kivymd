
from kivy.graphics import Rectangle
from kivy.atlas import Atlas

from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.vector import*
def atlas_to_list(atlas):
		x=[]
		for i in atlas.textures.values():
			x.append(i)
		return x
class MyBullet(Rectangle):
	def __init__(self,vx=3,vy=0,atlas=None,**k):
		super().__init__(**k)
		self.vx=vx
		self.vy=vy
		self.i=0
		self.atlas=atlas

		#print(atlas_to_list(self.atlas))
		self.texture=atlas_to_list(self.atlas)[0]

		#Clock.schedule_interval(self.animation,1/60)
	def animation(self,dt):
		if self.i==len(atlas_to_list(self.atlas)):
			self.i=0

		self.texture=atlas_to_list(self.atlas)[self.i]


		self.pos=Vector(self.vx,self.vy)+self.pos
		#self.i+=1

class Foe(Rectangle):
	def __init__(self,vx=0,vy=0,atlas=[],**k):
		super().__init__(**k)
		self.vx=vx
		self.vy=vy
		self.i=0
		self.size=self.texture.size
	
		self.idle=atlas[0]
		self.hit=atlas[1]
		#self.atlas=[]
		self.atlas=self.idle

		#print(atlas_to_list(self.atlas))
		#self.texture=atlas_to_list(self.atlas)[0]
		

		#Clock.schedule_interval(self.animation,1/5)

	def call_idle(self):
		self.i=0
		self.atlas=self.idle
	def call_hit(self):
		self.i=0
		self.atlas=self.hit
	def animation(self,dt):
		print('foe ani')
	
		#if self.i==len(atlas_to_list(self.atlas)):
		#	self.i=0
		


		self.texture=atlas_to_list(self.atlas)[self.i]

		

		#self.pos=Vector(self.vx,self.vy)+self.pos
		self.i+=1
		if self.i==len(atlas_to_list(self.atlas)):
			self.i=0
		#self.texture.flip_vertical()
		




class Coin(Rectangle):
	def __init__(self,vx=0,vy=0,atlas=None,**k):
		super().__init__(**k)
		self.vx=vx
		self.vy=vy
		self.i=0
	
	
		#self.atlas=[]
		self.atlas=atlas

		#print(atlas_to_list(self.atlas))
		self.texture=atlas_to_list(self.atlas)[0]
		

		Clock.schedule_interval(self.animation,1/5)


	def animation(self,dt):
	
		if self.i==len(atlas_to_list(self.atlas)):
			self.i=0
		

		self.texture=atlas_to_list(self.atlas)[self.i]

		

		#self.pos=Vector(self.vx,self.vy)+self.pos
		self.i+=1
		
		



class MyPlane(Rectangle):
	def __init__(self,vx=0,vy=0,**k):
		super().__init__(**k)
		self.vx=vx
		self.vy=vy
		self.i=0
		self.fire=False
		self.active=True
		self.fly=Atlas('res/fly/fly.atlas')
		self.shoot=Atlas('res/shoot/shoot.atlas')
		self.dead_texture=Image(source='res/trans.png').texture
		self.bool_fire=0
		self.bool_fly=1

		#self.atlas=[]
		self.atlas=self.fly
		#print(atlas_to_list(self.atlas))
		self.texture=atlas_to_list(self.atlas)[0]
		

		#Clock.schedule_interval(self.animation,1/30)

	def call_fire(self):
		self.bool_fire=1
		self.i=0
		self.atlas=self.shoot
	def call_fly(self):
		self.bool_fire=0
		self.i=0
		self.atlas=self.fly
	def animation(self,dt):
		# _list=atlas_to_list(self.atlas)
		# if self.active ==False:
		# 	if self.bool_fire==0:
		# 		_list=atlas_to_list(self.atlas)
		# 		_list.extend([self.dead_texture])
		# 	else:
		# 		_list=atlas_to_list(self.atlas)
		# 		_list.extend([self.dead_texture,self.dead_texture,self.dead_texture,self.dead_texture,self.dead_texture,self.dead_texture])
		# 		print('f0000')

		# else:
		_list=atlas_to_list(self.atlas)


	
	
		if self.i==len(_list):
			self.i=0
		

		self.texture=_list[self.i]

		

		#self.pos=Vector(self.vx,self.vy)+self.pos
		self.i+=1
		if self.i==len(_list):
			self.i=0
			


			
