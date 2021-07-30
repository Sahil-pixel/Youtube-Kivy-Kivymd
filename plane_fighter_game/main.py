from kivy.graphics import*
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from random import random,choice
from kivy.properties import*
from kivy.vector import*
from math import*
from random import random,randint,choice
from kivy.uix.widget import*
from kivy.app import App
from kivy.uix.relativelayout import*
from kivy.vector import*
from kivy.atlas import Atlas
from kivy.graphics.instructions import Canvas
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from functools import partial
from kivy.graphics.context_instructions import PopMatrix, PushMatrix, Rotate
from kivy.modules import monitor
from uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.animation import Animation 
from kivy.uix.label import*
from kivy.properties import*
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager,Screen
LabelBase.register(name="pacifico",
fn_regular="res/pacifico/Pacifico.ttf")

from graphics_classes import*

fps=60
monsters='res/monsters/'
def atlas_to_list(atlas):
		x=[]
		for i in atlas.textures.values():
			x.append(i)
		return x







class Pop(ModalView):
	def __init__(self,obj,**k):
		super().__init__(**k)
		self.obj=obj
		self.size_hint=(None,None)
		self.size=(0,0)
		self.auto_dismiss=False
		self.add_widget(Button(text='hello',on_release=self.callback))

	def callback(self,obj):
		self.obj.running=True
		self.obj.canvas.add(MyPlane(pos=self.obj.plane_pos,size=self.obj.plane_size))
		
		self.dismiss()
	def on_open(self,*a):
		print(a)
		a=Animation(size=(500,500),d=2)
		a.start(self)
	def on_dismiss(self):pass
		#self.size=(0,0)






		

class MainWidget(Widget):
	score=NumericProperty(0)
	life=NumericProperty(10)
	plane_animation_count=0
	foe_animation_count=0

	def __init__(self,**kwarg):
		super().__init__(**kwarg)
		print(monitor)
		self.running=False
		self.count_foe=[]
		self.count_coin=[]
		self.score=0
		#self.life=3
		#######sprites
		self.abullet=Atlas('res/bullet_atlas/myatlas.atlas')
		self.idle=Atlas('res/foe/idle/idle.atlas')
		self.hit=Atlas('res/foe/hit/hit.atlas')
		self.gdead=Atlas('res/round_ghost/round_ghost_dead/gdead.atlas')
		self.gidle=Atlas('res/round_ghost/round_ghost_idle/gidle.atlas')
		self.pidle=Atlas(monsters+'pink/idle/pink_idle.atlas')
		self.phit=Atlas(monsters+'pink/gothit/pink_hit.atlas')
		self.oidle=Atlas(monsters+'orange/idle/orange_idle.atlas')
		self.ohit=Atlas(monsters+'orange/gothit/orange_hit.atlas')


		self.coin_atlas=Atlas('res/GoldCoinSprite/coin.atlas')

		self.foe_atlas=[[self.idle,self.hit],[self.gidle,self.gdead],[self.pidle,self.phit],[self.oidle,self.ohit]]
	
		self.ct=Image(source='res/cloud.png').texture
		self.ft2=Image(source='res/flo.png').texture
		_path='res/floor/png/Objects/'
		self.ft=Image(source=_path+'Cactus1.png').texture

		##path of floor floder
		
		self.ft_array=[]
		
		self.loop_time=0

		with self.canvas.before:
			Color(0,0.85,1)

			self.rect=Rectangle(pos=self.pos,size=self.size,source='res/png/BG.png')
			Color(1,1,1)
			self.cloud=Rectangle(pos=(self.pos[0],self.top-100),size=(self.width,100))
			self.floor=Rectangle(pos=self.pos,size=self.size)
		with self.canvas:
			self.floor2=Rectangle(pos=self.pos,size=(self.width,100))



		self._bullet_count=0
       ######button bools 
		self._btn_down=False
		self._btn_left=False
		self._btn_right=False
		self._btn_up=False
		self._btn_fire=False


		#with self.canvas.after:
		#	Color(rgba=(1,0,0,0.3))
		delta=100
		self.btn_left=Button(pos=(delta-50,100),size=(100,100),background_color=(1,1,1,0.3))
			
		self.btn_right=Button(pos=(delta+250,100),size=(100,100),background_color=(1,1,1,0.3))
		
		self.btn_up=Button(pos=(delta+100,200),size=(100,100),background_color=(1,1,1,0.3))
			
		self.btn_down=Button(pos=(delta+100,0),size=(100,100),background_color=(1,1,1,0.3))
		self.btn_fire=Button(pos=(self.width-200,100),size=(100,100),background_color=(1,1,1,0.3))
		self.btn_up.bind(state=partial(self.btn_state_callback,'_btn_up'))
		self.btn_down.bind(state=partial(self.btn_state_callback,'_btn_down'))
		self.btn_right.bind(state=partial(self.btn_state_callback,'_btn_right'))
		self.btn_left.bind(state=partial(self.btn_state_callback,'_btn_left'))
		self.btn_fire.bind(state=partial(self.btn_state_callback,'_btn_fire'))



		###########
		#upper widets 
		self.score_label=Label(size=(200,50),pos=(0,self.height-50),text=str(self.score),color=[0,0,1,1],font_name='pacifico',font_size=50)
		self.life_label=Label(size=(200,50),pos=(self.width/2,self.height-50),text=str(self.life),font_name='pacifico',font_size=50)


		

		self.bind(pos=self._update_rect,size=self._update_rect)
		Clock.schedule_once(self.init2,)
		Clock.schedule_interval(self.game_loop,1/fps)

	def on_life(self,*a):
		self.life_label.text=str(a[1])
	def on_score(self,*a):
		self.score_label.text=str(a[1])

	def btn_callback_r(self,btn_bool,obj,state):
		if state=='down':pass


	
	
		

	def btn_state_callback(self,btn_bool,obj,state):
		if state=='down':
			if btn_bool=='_btn_left':
				self._btn_left=True
			if btn_bool=='_btn_right':
				self._btn_right=True
			if btn_bool=='_btn_up':
				self._btn_up=True
			if btn_bool=='_btn_down':
				self._btn_down=True
			if btn_bool=='_btn_fire':
				self._btn_fire=True
		if state=='normal':

			if btn_bool=='_btn_left':
				self._btn_left=False
			if btn_bool=='_btn_right':
				self._btn_right=False
			if btn_bool=='_btn_up':
				self._btn_up=False
			if btn_bool=='_btn_down':
				self._btn_down=False
			if btn_bool=='_btn_fire':
				self._btn_fire=False
				for i in self.canvas.children:
					if isinstance(i, MyPlane):
						i.call_fly()

		
	
			
		
	


	def init2(self,dt):
		print(self.size)
		self.add_widget(self.btn_up)
		self.add_widget(self.btn_down)
		self.add_widget(self.btn_left)
		self.add_widget(self.btn_right)
		self.add_widget(self.btn_fire)
		self.add_widget(self.score_label)
		self.add_widget(self.life_label)
		
		

		
		self.ct.wrap='repeat'
		self.ft2.wrap='repeat'
		self.ft.wrap='repeat'
		self.ct.uvsize=(self.width/self.ct.width,-1)
		self.ft2.uvsize=(self.width/self.ft2.width,-1)
		self.ft.uvsize=(self.width/self.ft.width,-1)
		
		



		self.cloud.texture=self.ct
		self.floor.texture=self.ft
		self.floor2.texture=self.ft2
		self.plane_size=(100,80)
		self.plane_pos=(200,100+self.height/2)

		#self.canvas.add(MyBullet(pos=(200+100,200),size=(20,20)))
		self.plane_obj=MyPlane(pos=self.plane_pos,size=self.plane_size)
		self.canvas.add(self.plane_obj)
		self.previous_x=self.width
		

	def atlas_to_list(self,atlas):
		x=[]
		for i in atlas.textures.values():
			x.append(i)
		return x

	def _update_rect(self,instance,value):
		self.rect.pos=instance.pos
		self.rect.size=instance.size
		self.cloud.pos=(instance.pos[0],instance.top-100)
		self.cloud.size=(instance.width,100)
		self.floor.pos=(instance.pos[0],0)
		self.floor.size=(instance.width,200)
		self.floor2.pos=instance.pos
		self.floor2.size=(instance.width,100)
		self.btn_fire.pos=(self.width-200,100)   
		self.score_label.pos=(0,self.height-50)  
		self.life_label.pos=(self.width/2,self.height-50) 
		self.ct.uvsize=(self.width/self.ct.width,-1)
		self.ft2.uvsize=(self.width/self.ft2.width,-1)
		self.ft.uvsize=(self.width/self.ft.width,-1)




		self.h=self.height
		self.w=self.width
	def game_over(self):
		self.running=False
		self.loop_time=0
		self.score=0
		self.canvas.clear()
	def game_pause(self):
		self.running=False

		######temporary reset
	def restart_game(self):
		self.canvas.add(self.floor2)
		self.canvas.add(Color(1,1,1))
		self._btn_down=False
		self._btn_left=False
		self._btn_right=False
		self._btn_up=False
		self._btn_fire=False

		self.add_widget(self.btn_up)
		self.add_widget(self.btn_down)
		self.add_widget(self.btn_left)
		self.add_widget(self.btn_right)
		self.add_widget(self.btn_fire)
		self.add_widget(self.score_label)
		self.add_widget(self.life_label)


	def datect_object_from_list(self,obj):
		for i in self.canvas.children:
			if isinstance(i, obj):
				return True
	def detect_point_collision(self,point,obj):
		if point[0]>obj.pos[0] and point[0]<obj.pos[0]+obj.size[0]:
			if point[1]>obj.pos[1] and point[1]<obj.pos[1]+obj.size[1]:
				return True
		return False



	def detect_collision(self,i,j):
		if i.pos[0]+i.size[0]>=j.pos[0] and j.pos[0]+j.size[0]>=i.pos[0]:
			if i.pos[1]+i.size[1]>=j.pos[1] and j.pos[1]+j.size[1]>=i.pos[1]:
				return True
		return False
	def _set_pos(self,i,p,r):
		if r ==1:
			return (p+100,(self.height/2)+sin((i*50)*pi/180)*200)
		if r==2:
			return (p+100,100+50*i)
		else:
			return(p+100,i*50)


	



	def my_plane_blink_deactive(self,i,dt):
		i.active=True

	def callback_after_some_time(self,j,dt):
		self.canvas.remove(j)


	def game_loop(self,dt):

		if self.running:
			####plane animation
			if self.plane_animation_count>fps/20:
				self.plane_obj.animation( dt)
				print(self.plane_animation_count)
				self.plane_animation_count=0
			######foe animaion
			if self.foe_animation_count>fps/5:
				for j in self.canvas.children:
					if isinstance(j, Foe):
						j.animation(dt)

				self.foe_animation_count=0




			self.count_foe=[]
			self.count_coin=[]


		#print(self.ct.uvpos[0]+dt)
			self.ct.uvpos=((self.ct.uvpos[0]+1.2*dt)%self.width,self.ct.uvpos[1])
			self.ft.uvpos=((self.ft.uvpos[0]+0.3*dt)%self.width,self.ft.uvpos[1])
			self.ft2.uvpos=((self.ft2.uvpos[0]+1.2*dt)%self.width,self.ft2.uvpos[1])


			self.cloud.texture=self.ct
			self.floor.texture=self.ft
			self.floor2.texture=self.ft2





			for i in self.canvas.children:
				if isinstance(i, Coin):
					self.count_coin.append(i)


			
				if isinstance(i,Foe):

					self.count_foe.append(i)


			if len(self.count_coin)<=0:
				for i in range(20):
					self.canvas.add(Coin(atlas=self.coin_atlas,vx=-randint(1,5),vy=randint(1,5),pos=(self.width+50*i,i),size=(50,50)))

			if len(self.count_foe)<=0:
				_velo_y=randint(-2,2)
				if randint(0, 1)==1:
					for i in range(randint(5,20)):
						self.canvas.add(Foe(atlas=choice(self.foe_atlas) ,vx=-randint(1,10),vy=_velo_y,pos=(self.width+100*i,((20-i)/20)*self.height),size=(50,50)))
				_velo_y=randint(-10,10)
				_velo_x=randint(-6,-1)

				r=randint(1, 2)
				atlas=choice(self.foe_atlas)
				for i in range(randint(10,50)):
					pobj=Foe(atlas=atlas,vx=_velo_x,vy=_velo_y,pos=self._set_pos(i, self.previous_x,r))				
					self.canvas.add(pobj )
					#self.canvas.add(Foe(atlas=[self.gidle,self.gdead],vx=-1,vy=1,pos=(self.width+100*i,(20-i)*50),size=(50,50)))
					self.previous_x=pobj.pos[0]


            
			for i in self.canvas.children:
				if isinstance(i, MyPlane):

					######coin 
					for j in self.canvas.children:
						if isinstance(j, Coin):
							if self.detect_collision(i, j):
								self.canvas.remove(j)
								self.score+=10
								#Pop(self,size=(0,0)).open(animation=1,)
								#self.clear_widgets()
								#self.game_over()
								#self.running=0
								#j.call_hit()
								#j.vx=0
								#j.vy=-1
								print('collision with coin',self.score)


					####FIRE 
					if self._btn_fire:
						if self._bullet_count>10:
							#self.canvas.add(MyBullet(vx=10,vy=-10,atlas=self.abullet,pos=(i.pos[0] +i.size[0],i.pos[1]+10),size=(20,20)))
							self.canvas.add(MyBullet(vx=10,atlas=self.abullet,pos=(i.pos[0] +i.size[0],i.pos[1]+10),size=(20,20)))
							#self.canvas.add(MyBullet(vx=10,vy=10,atlas=self.abullet,pos=(i.pos[0] +i.size[0],i.pos[1]+10),size=(20,20)))
							i.call_fire()
							self._bullet_count=0


					####### plane control
					if self._btn_down:
						i.pos=Vector(0,-10)+i.pos
					if self._btn_up:
						i.pos=Vector(0,10)+i.pos
					if self._btn_right:
						i.pos=Vector(10,0)+i.pos
					if self._btn_left:
						i.pos=Vector(-10,0)+i.pos

			








					#####Foe
					for j in self.canvas.children:
						if isinstance(j, Foe):
							
							if self.detect_collision(i, j):
								self.canvas.remove(j)
								if i.active: 
									self.life-=1
									i.active=False
									#self.canvas.add(Color(rgba=(1,0,0,1)))
									Clock.schedule_once(partial(self.my_plane_blink_deactive,i),4)
								#Pop(self,size=(0,0)).open(animation=1,)
								#self.clear_widgets()
								#self.game_over()
								#self.running=0
								#j.call_hit()
								#j.vx=0
								#j.vy=-1
								print('collision with plane')
								#Clock.schedule_once(partial(self.callback_after_some_time,j),1)



				if isinstance(i, MyBullet):
					for j in self.canvas.children:
						if isinstance(j, Foe):
							if self.detect_collision(i, j):
								self.canvas.remove(i)
								j.call_hit()
								j.vx=0
								j.vy=-1
								print('collson')
								Clock.schedule_once(partial(self.callback_after_some_time,j),1)





				if isinstance(i, Foe):
					i.pos=Vector(i.vx,i.vy)+i.pos

					if i.pos[0]+i.size[1]<0:
						self.canvas.remove(i)




					
					if i.pos[1]<0 or i.pos[1]>self.height:
						i.vy*=-1


				if isinstance(i, Coin):
					i.pos=Vector(i.vx,i.vy)+i.pos

					if i.pos[0]+i.size[1]<0:
						self.canvas.remove(i)




					
					if i.pos[1]<0 or i.pos[1]>self.height:
						i.vy*=-1




				if isinstance(i, MyBullet):

					i.animation(dt)
					
					if i.pos[0]>self.width or i.pos[1]<0 or i.pos[1]>self.height:
						self.canvas.remove(i)




			###ELEMINATE
			self.loop_time+=dt
			self._bullet_count+=1
			self.plane_animation_count+=1
			self.foe_animation_count+=1


			#print(self.loop_time)
			#####game over section
			if self.life==0:
				self.game_over()







































































	def _on_touch_down(self,touch):
		if self.collide_point(*touch.pos):
			if self.running:

				#######buttomns 

				if self.detect_point_collision(touch.pos,self.btn_up):
					print('btnup')
					self._btn_up=True

				if self.detect_point_collision(touch.pos,self.btn_down):
					self._btn_down=True
					print('btn down')
				if self.detect_point_collision(touch.pos,self.btn_right):
					print('bt right')


					self._btn_right=True

				if self.detect_point_collision(touch.pos,self.btn_left):
					print('left')
					self._btn_left=True

				if self.detect_point_collision(touch.pos,self.btn_fire):
					print('firing')
					self._btn_fire=True



					#####################
				


			#print(touch.button)
				#if touch.pos[0]>self.width/2:

					
					#for i in self.canvas.children:
						#if isinstance(i, MyPlane):
							
				#else:
					#self.initialtouch=touch.pos[1]
					#self.initialtouch_x=touch.pos[0]


	
	def _on_touch_up(self,touch):



		if self.collide_point(*touch.pos):
			if self.running:
				if self.detect_point_collision(touch.pos,self.btn_up):
				#print('btnup')
					self._btn_up=False

				if self.detect_point_collision(touch.pos,self.btn_down):
					self._btn_down=False
				#print('btn down')
				if self.detect_point_collision(touch.pos,self.btn_right):
					#print('bt right')


					self._btn_right=False
				if self.detect_point_collision(touch.pos,self.btn_left):
					#print('bt left')
					self._btn_left=False
					



				if self.detect_point_collision(touch.pos,self.btn_fire):
					self._btn_fire=False

				
			
				'''
					self.finaltouch=touch.pos[1]
					if (self.finaltouch-self.initialtouch)>0:
						print('+')
						for i in self.canvas.children:
							if isinstance(i, MyPlane):
								i.pos=Vector(0,2)+i.pos
					else:
						print('-')
				'''

	

	def _on_touch_move(self,touch):

		


		if self.collide_point(*touch.pos):
			print(touch.dx)
			if self.running:
				if self.detect_point_collision(touch.pos,self.btn_up):
				#print('btnup')
					self._btn_up=False

				if self.detect_point_collision(touch.pos,self.btn_down):
					self._btn_down=False
				#print('btn down')
				if self.detect_point_collision(touch.pos,self.btn_right):
					#print('bt right')


					self._btn_right=False
				if self.detect_point_collision(touch.pos,self.btn_left):
					#print('bt left')
					self._btn_left=False
					



				if self.detect_point_collision(touch.pos,self.btn_fire):
					self._btn_fire=False
			
				



				
					#self.finaltouch=touch.pos[1]
					#self.finaltouch_x=touch.pos[0]
					#print(touch.button)
				
			'''

					if touch.dx>10:
						for i in self.canvas.children:
							if isinstance(i, MyPlane):
								i.pos=Vector(+10,0)+i.pos
						print('right')
					if touch.dx<-10:
						for i in self.canvas.children:
							if isinstance(i, MyPlane):
								i.pos=Vector(-10,0)+i.pos
						print('left')

				
		

		
			


				if touch.dy>10:
					print('+')
					for i in self.canvas.children:
						if isinstance(i, MyPlane):
							i.pos=Vector(0,10)+i.pos
				if touch.dy<-10:
					print('-')
					for i in self.canvas.children:
						if isinstance(i, MyPlane):
							i.pos=Vector(0,-10)+i.pos

			'''

			







			#self.canvas.add(MyBullet(pos=(200+100,200),size=(50,50)))




		







class GScreen(Screen):
	def __init__(self,**k):
		super().__init__(**k)
		#self.rw=RelativeLayout()
		self.game_wid=MainWidget()
		#self.rw.add_widget(self.game_wid)
		self.add_widget(self.game_wid)
	def on_pre_enter(self,*a):
		self.game_wid.running=True



class  MainMenu(Screen):
	def __init__(self,**k):
		super().__init__(**k)
		self.box=BoxLayout(orientation='vertical',padding=10,spacing=20)
		with self.canvas.before:
			self.rect=Rectangle(pos=self.pos,size=self.size,source='res/floor/png/BG.png')
		self.box.add_widget(Button(text='NewGame',font_size=40,color=(1,0,0,1),font_name='pacifico',on_release=self._callback,background_color=(1,1,1,0)))
		self.box.add_widget(Button(text='ABOUT',font_size=40,background_color=(1,1,1,0)))
		self.box.add_widget(Button(background_color=(1,1,1,0)))
		self.add_widget(self.box)
		self.bind(pos=self._update_rect,size=self._update_rect)

	def _update_rect(self,instance,value):
		self.rect.pos=instance.pos
		self.rect.size=instance.size
		#print('###############',instance,value)

	def _callback(self,obj):
		self.parent.current='gscreen'





class About(Screen):
	def __init__(self,**k):
		super().__init__(**k)






class Manage(ScreenManager):
	def __init__(self,**k):
		super().__init__(**k)
		
		self.add_widget(MainMenu(name='mainmenu'))
		self.add_widget(GScreen(name='gscreen'))
		self.add_widget(About(name='about'))










































































from array import array


class MyWidget(Widget):


	def __init__(self,**k):		

		super().__init__(**k)
		self.t=0
		texture = Texture.create(size=(64, 64))
		size = 64 * 64 * 3
		buf = [int(x * 255 / size) for x in range(size)]
		print(buf)
		buf =  array('B', buf)
		bu=buf
		print(bu)
		texture.blit_buffer(bu, colorfmt='rgb', bufferfmt='ubyte')
		self.texture1=Image(source='back4.png').texture
		self.texture1.wrap='repeat'
		self.texture1.uvsize=(1,-1)
		self.texture3=Image(source='BG.png').texture
		texture2=Image(source='BG.png').texture
		texture2.wrap='repeat'

		print(self.texture1.size)


		


	








		with self.canvas.before:
			Color(1,1,1)

			self.rect1=Rectangle(pos=self.pos,size=(self.texture1.size[0],self.size[1]),texture=self.texture1,)
		self.rect2=Rectangle(pos=self.pos,size=(texture2.size[0],self.size[1]),texture=texture2,tex_coords=(0,1,2,1,2,0,0,0))


		

		self.bind(pos=self._update_rect,size=self._update_rect)
		Clock.schedule_once(self.init2,0)
		self.mx=0
		Clock.schedule_interval(self.update_call,1/60)




	def init2(self,dt):
		#Clock.schedule_interval(self.update_foe_fire,1/1)
		self.h=self.height
		self.w=self.width
		h=self.h
		w=self.w
		

	
		
	def _update_rect(self,instance,value):
		self.rect1.pos=instance.pos
		self.rect1.size=(self.rect1.size[0],instance.size[1])
		self.rect2.pos=instance.pos
		self.rect2.size=(self.rect1.size[0],instance.size[1])



		self.h=self.height
		self.w=self.width
		

	def update_call(self,dt):
		#self.canvas.before.clear()
		self.t+=dt
		mybox_list=[]


		rel_x=self.mx%self.rect1.size[0]
		self.texture1.uvpos=(self.texture1.uvpos[0]+0.1*dt,self.texture1.uvpos[1])
		self.rect1.texture=self.texture1
		if self.t>10:
			size = 64 * 64 * 3
			buf = [int(x * 255 / size) for x in range(size)]
			arr = array('B', buf)
			#self.texture1.flip_horizontal()



		#self.rect1.pos=(rel_x-self.rect1.size[0],self.rect1.pos[1])
		#self.canvas.before.add(Color(1,1,1))
		#self.canvas.before.add(self.rect1)
		#if rel_x<self.width:
		
				
				
			#self.rect2.pos=(rel_x-10,self.rect2.pos[1])
			#self.canvas.before.add(self.rect2)


		print('hello')
		print(self.texture1.tex_coords)
		#self.mx-=5
		#print(rel_x)
		

		

class FboTest(Widget):
	def __init__(self, **kwargs):
		super(FboTest, self).__init__(**kwargs)
		with self.canvas:
			self.fbo = Fbo(size=(300, 500))
			self.fbo.texture.wrap='repeat'	
			self.fbo.texture.uvsize=(1,-1)

			Color(1, 1, 1)
			#Rectangle(size=(32, 32), texture=self.fbo.texture)
			#Rectangle(pos=(32, 0), size=(64, 64), texture=self.fbo.texture)
			self.r=Rectangle(pos=(96, 0), size=(5000, 800), texture=self.fbo.texture)

			# in the second step, you can draw whatever you want on the fbo
		with self.fbo:
			Color(1, 1, 1, 1)
			Rectangle(pos=(0,100),size=(100, 256),source='res/BG.png')
			Color(1, 1, 1, 1)
			Rectangle(pos=(100,100),size=(100, 256),source='BG.png')
			Rectangle(pos=(200,100),size=(100, 256),source='back4.png')
			Rectangle(pos=(300,100),size=(100, 256),source='back4.png')
		self.fbo.texture.wrap='repeat'	
		self.fbo.texture.uvsize=(1,1)
		Clock.schedule_interval(self.update_call,1/60)
		self.t=0


	def update_call(self,dt):
		#self.canvas.before.clear()
		self.t+=dt
		mybox_list=[]


		#rel_x=self.mx%self.rect1.size[0]
		self.fbo.texture.uvpos=(self.fbo.texture.uvpos[0]+0.5*dt,self.fbo.texture.uvpos[1])
		self.r.texture=self.fbo.texture
			#self.texture1.flip_horizontal()



		#self.rect1.pos=(rel_x-self.rect1.size[0],self.rect1.pos[1])
		#self.canvas.before.add(Color(1,1,1))
		#self.canvas.before.add(self.rect1)
		#if rel_x<self.width:
		
				
				
			#self.rect2.pos=(rel_x-10,self.rect2.pos[1])
			#self.canvas.before.add(self.rect2)


		print('hello')
		#print(self.texture1.tex_coords)
		#self.mx-=5














		

	

class MyPaintApp(App):
	def build(self):
		return Manage()
	



if __name__ == '__main__':
    MyPaintApp().run()
 
 
