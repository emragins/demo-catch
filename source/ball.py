import movingentity
import collisions
import ika


class Ball(movingentity.MovingEntity):
	def __init__(self, x, y, type = 'ball'):
		movingentity.MovingEntity.__init__(self,x,y, type)
		
		
		#these aren't exactly accurate...
		#these essentially represent x_vel and y_vel
		#	will update when the ball gets thrown
		#	well reset when ball stops moving
		self.moveSpeed = 0
		self.jumpStrength = 0
		self.heldBy = None
		self.thrown = False
		self.floorFriction = 1
		
	def Update(self):
		if not self.IsHeld():
			movingentity.MovingEntity.Update(self)
		else:
			self.realX = self.heldBy.realX + self.heldBy.hotX + int(0.5*self.heldBy.hotW)
			self.realY = self.heldBy.realY + self.heldBy.hotY
		
		if self.IsThrown():
			if not self.IsFalling() and not self.IsJumping():
				self.moveSpeed -= self.floorFriction
			if self.moveSpeed is 0:
				self.SetState('Wait')
				self.thrown = False
	
	def Render(self):
		if self.heldBy is None:
			movingentity.MovingEntity.Render(self)
		#otherwise don't be visible...
	
	def BecomesThrown(self, x_vel, y_vel):
		self.heldBy = None
		self.thrown = True
		
		self.jumpStrength = y_vel
		
		self.StartJumping()
		
		self.moveSpeed = abs(x_vel)
		if x_vel > 0:
			self.SetState('MoveRight')
		else:
			self.SetState('MoveLeft')
	
	def BecomesHeld(self, heldBy):
		#for when caught mid-air
		self.StopJumping()
		self.StopFalling()
		self.ResetGravity()
		self.thrown = False
		self.heldBy = heldBy
	
	def IsHeld(self):
		
		if self.heldBy is not None:
			return True
		return False
	def IsThrown(self):
		return self.thrown
		