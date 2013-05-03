import movingentity
import collisions
from data import data
import math
import ballthrower

class BallMech(movingentity.MovingEntity, ballthrower.BallThrower):
	def __init__(self, x, y, type = 'ballmech'):
		movingentity.MovingEntity.__init__(self,x,y, type)
		ballthrower.BallThrower.__init__(self)
		
		self.moveSpeed = 3
		self.aiTimer = 0
		self.aiTimerMax = 7
		self.jumpStrength = 6
		self.dx = 0
		self.dy = 0
		self.hitWall = False
		self.ballYMin = 2
		
	def Update(self):
		movingentity.MovingEntity.Update(self)
		
		
		if self.aiTimer >= self.aiTimerMax:
			self.UpdateAI()
			self.aiTimer = 0
		self.aiTimer += 1
			
		self.ExecuteAI()
	
		ballthrower.BallThrower.Update(self)
	
	def UpdateAI(self):
		#retrieve ball
		if not self.holdsBall:
			#find the ball
			ball = self.FindNearestBall()
			if ball is None:
				self.DoNothing()
				return
			else:
			#see if the nearest is closer to the player
				closer = self.CloserThanPlayer(ball)
				if not closer:
					self.DoNothing()
					return
			self.dx, self.dy = self.DistanceToObject(ball)
			if abs(self.dy) > 16 and abs(self.dx) <=5:	##really not best way to do this
				self.MoveLeftBy(8)	#in case sitting on cliff over ball
		else:
			self.DoNothing()
			#self.GetOutOfDitch()
			dx,dy = self.DistanceToObject(data.player)	#will use player's top left hot coords
			x_vel = 0.5*dx/16	#tilesize
			
			if x_vel is not 0:
				t = abs(dx/x_vel) - 4
				y_vel = int(-dy/t + (t)/4)
			else:
				y_vel = 5	#doesn't matter if x = 0 
			x_vel = int(x_vel)
			#dy = -dy/16	#tilesize
			
			#if y < self.ballYMin:
			#	y = self.ballYMin
			#y = int(2*y)
			
			self.ThrowBall(x_vel,y_vel)
		
	def ExecuteAI(self):
		if self.hitWall:
			self.StartJumping()
		else:
			self.StopJumping()
			
		if self.dx < 0:
			self.SetState('MoveLeft')
		elif self.dx > 0:
			self.SetState('MoveRight')
		else:
			self.SetState('Wait')
		
	def FindNearestBall(self):
		ballList = []
		for obj in data.objects:
			if hasattr(obj, 'IsHeld'):
				if not obj.IsHeld():
					ballList.append(obj)
		
		if len(ballList) is 0:
			return None
		
		dist = 500	##cheating
		ball = None
		for tempball in ballList:
			tempDist = self.DiagonalDistanceToObject(tempball)
			if tempDist < dist:
				dist = tempDist
				ball = tempball
				
		return ball
		
	def DiagonalDistanceToObject(self, ball):
		dx = abs(ball.realX - self.realX)
		dy = abs(ball.realY - self.realY)
		
		dist = math.sqrt(dx^2 + dy^2)
		return dist
	
	def DistanceToObject(self, obj):
		dx = (obj.realX + obj.hotX + int(.5*obj.hotW)) - (self.realX + int(.5*self.hotW))
		dy = (obj.realY + obj.hotY) - self.realY
		
		return dx, dy
		
		
		
	def CloserThanPlayer(self, obj):
		dx1 = abs(obj.realX - self.realX)
		'''
		dy = abs(obj.realY - self.realY)
		
		distSelf = math.sqrt(dx^2 + dy^2)
		'''
		player = data.player
		
		dx2 = abs(obj.realX - (player.realX + player.hotX))
		'''
		dy = abs(obj.realY - (player.realY + player.hotY))
		
		distPlayer = math.sqrt(dx^2 + dy^2)
		'''
		if dx1 <= dx2:
			return True
		return False
		
	def DoNothing(self):
		self.SetState('Wait')
		self.dx = 0
		self.dy = 0
		self.hitWall = False