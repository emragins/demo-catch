import collisions

class BallThrower(object):
	def __init__(self):
		self.holdsBall = None
		self.hitBall = False
		
		#so the ball isn't caught as soon as it's released
		self.throwTimer = 10
		self.throwTimerMax = 10
	
	def Update(self):
		if self.holdsBall:
			return
		
		if self.throwTimer < self.throwTimerMax:
			self.throwTimer += 1
			return
				
		ball = collisions.CheckCollisionsBalls(self)
				
		if ball is None:
			return
		
		self.HoldsBall(ball)
		
	def HoldsBall(self, ball):
		self.holdsBall = ball
		ball.BecomesHeld(self)
	
	def ThrowBall(self, xvel, yvel):
		self.throwTimer = 0
		if self.holdsBall is None: #error checking
			return
		self.SetState('Throw')
		self.holdsBall.BecomesThrown(xvel, yvel)
		self.holdsBall = None
		
	
	