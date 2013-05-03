
import collisions
#from data import configdata #need for quadrant checking
		
class PositionHandler(object):
	def __init__(self):
		self.states = {
			'MoveLeft': self.MoveLeft,
			'MoveRight': self.MoveRight,
			'Wait': self.Wait,
			'Jump': self.Jump,
			'Fall': self.Wait,	#for sprite
			'GrabLeft': self.Wait,	#for sprite
			'GrabRight': self.Wait,	#for sprite
			'Throw': self.Wait,
			None: self.Wait
			
			}
		
		self.vertNegativeSpeed = 1 #positive is down
		self.gravityTimer = 0
		self.gravityEffect = 1
		self.lastGravityCollision = None
		
		
		
	def Update(self):
		state = self.states[self.GetState()]
		state()
		for state in self.extraStates:
			self.states[state]()
		self.ApplyGravity()	
		
	def Wait(self):
		pass	
	
	"""
	hasattr...
	need to return somehow to player and enemies (for ai purposes) what it collided with. 
	player will need blocks and items, enemies will need anything solid so they can turn around if moving, or climb even
	
	could maybe be more specific instead of just "collidesWith" could use "collidesWithBlock", "collidesWithItem" saving it from testing walls, too
	"""
	def MoveLeft(self):
		self.realX -= self.moveSpeed	
		col = collisions.CheckSolidCollisionsForMovement(self)
		self.IfHasHitWall(col)
		if hasattr(col, "realX"):
			while self.CollidesWith(col):  ##might break if collision adjustment moves from one object to the next
				self.realX += 1
		else:
			while collisions.CheckSolidCollisionsForMovement(self):
				self.realX += 1
				
	def MoveRight(self):
		self.realX += self.moveSpeed
		col = collisions.CheckSolidCollisionsForMovement(self)
		self.IfHasHitWall(col)
		if hasattr(col, "realX"):
			while self.CollidesWith(col):  ##might break if collision adjustment moves from one object to the next
				self.realX -= 1
		else:
			while collisions.CheckSolidCollisionsForMovement(self):
				self.realX -= 1
		
	
	
	"""Used for being moved by something other than interal power"""
	def MoveLeftBy(self, speed):
		self.realX -= speed	
		col = collisions.CheckSolidCollisionsForMovement(self)
		if hasattr(col, "realX"):
			while self.CollidesWith(col):  ##might break if collision adjustment moves from one object to the next
				self.realX += 1
		else:
			while collisions.CheckSolidCollisionsForMovement(self):
				self.realX += 1
		return col
	def MoveRightBy(self, speed):
		self.realX += speed
		col = collisions.CheckSolidCollisionsForMovement(self)
		if hasattr(col, "realX"):
			while self.CollidesWith(col):  ##might break if collision adjustment moves from one object to the next
				self.realX -= 1
		else:
			while collisions.CheckSolidCollisionsForMovement(self):
				self.realX -= 1
		return col
	
	def Jump(self):			
		#if self.jumpStrength <= self.vertNegativeSpeed:
		#	self.StopJumping() 
		#	return
			
		self.realY -= self.jumpStrength
		
		collides = collisions.CheckSolidCollisionsForMovement(self)
				
		if collides or not self.IsFalling():
			while collisions.CheckSolidCollisionsForMovement(self):
				self.realY += 1 #move down incrementally to get head out of ceiling
			self.StopJumping() #remove the state so that verticle propultion is 0 (ie. so it can just start falling)
						
	
	def ApplyGravity(self):
		self.realY += self.vertNegativeSpeed
		self.lastGravityCollision = collisions.CheckSolidCollisionsForGravity(self)
		while collisions.CheckSolidCollisionsForGravity(self):
			self.realY -= 1 #move up incrementally to 'land' on the ground
				
		if self.lastGravityCollision:
			self.ResetGravity()
			self.StopFalling()
		else:
			self.gravityTimer += 1
			self.StartFalling()
			if self.gravityTimer >= 3: 
				self.vertNegativeSpeed += self.gravityEffect
				self.gravityTimer = 0

	def ResetGravity(self):
		self.vertNegativeSpeed = 1
		self.gravityTimer = 0
		
	def IfHasHitWall(self, col):
		if hasattr(self, 'hitWall'):
			if col:
				self.hitWall = True
			else:
				self.hitWall = False
