import movingentity
import ballthrower
import timer

import ika #for input and hud


class Player(movingentity.MovingEntity, ballthrower.BallThrower):
	def __init__(self, x, y):
		movingentity.MovingEntity.__init__(self, x, y, type = 'player')
		ballthrower.BallThrower.__init__(self)
		
		self.moveSpeed = 4
		self.jumpStrength = 6
		
		self.ballXVel = 5
		self.ballYVel = 5
		
		self.font = ika.Font('fonts\\ocr_yellow.fnt')
		self.timer = timer.Timer(40)
		self.pressed = False
		
	def Update(self):
		kb = ika.Input.keyboard
		
			
		if kb['LEFT'].Position():
			self.SetState('MoveLeft')
		elif kb['RIGHT'].Position():
			self.SetState('MoveRight')
		else:
			self.SetState('Wait')
			
		if kb['UP'].Position():
			self.StartJumping()
		else:
			self.StopJumping()
		
		if kb['SPACE'].Pressed() and self.holdsBall:
			if self.direction == 'Left':
				self.ThrowBall(-self.ballXVel, self.ballYVel)
			else:
				self.ThrowBall(self.ballXVel, self.ballYVel)
			
		
		if kb['PAGEUP'].Position():
			if self.pressed == False:
				self.timer.Reset()
				self.pressed = True
				self.ballYVel += 1
				
			if self.pressed and self.timer.IsDone():
				self.ballYVel += 1
				
		if kb['PAGEDOWN'].Position():
			if self.pressed == False:
				self.timer.Reset()
				self.pressed = True
				if self.ballYVel == 0:
					pass
				else:
					self.ballYVel -= 1
				
			if self.pressed and self.timer.IsDone():
				self.ballYVel -= 1
				
		if kb['HOME'].Position():
			if self.pressed == False:
				self.timer.Reset()
				self.pressed = True
				self.ballXVel += 1
				
			if self.pressed and self.timer.IsDone():
				self.ballXVel += 1
				
		if kb['END'].Position():
			if self.pressed == False:
				self.timer.Reset()
				self.pressed = True
				if self.ballXVel == 0:
					pass
				else:
					self.ballXVel -= 1
				
			if self.pressed and self.timer.IsDone():
				self.ballXVel -= 1
		
		#reset 'pressed' position
		if kb["PAGEDOWN"].Position() == 0 \
			and kb["PAGEUP"].Position() == 0 \
			and kb["END"].Position() == 0 \
			and kb["HOME"].Position() == 0:
			self.pressed = False
		
		ballthrower.BallThrower.Update(self)
		movingentity.MovingEntity.Update(self)
	
	def Render(self):
		movingentity.MovingEntity.Render(self)
		
		##hud stuff doesn't really belong here... oh well.
		self.font.Print(10, 5, 'X Velocity: ' + str(self.ballXVel))
		self.font.Print(10, 20, 'Y Velocity: ' + str(self.ballYVel))
	
	
	def DropBlock(self):
		self.RemoveState("GrabLeft")
		self.RemoveState("GrabRight")
		self.grabbedBall = None
		
	
	
	