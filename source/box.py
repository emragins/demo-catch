"""
A class that defines a rectangular region. Mainly used for collision.
"""

class Box:
	
	def __init__ (self, realx, realy, hotx, hoty, hotw, hoth):
		self.realX = realx
		self.realY = realy
		self.hotX = hotx
		self.hotY = hoty
		self.hotW = hotw
		self.hotH = hoth
		
	def CollidesWith(self, box):
		#x_hits = self.realX + self.hotX + self.hotW >= box.realX + box.hotX and self.realX + self.hotX <= box.realX + box.hotW + box.hotX
		#y_hits = self.realY + self.hotY + self.hotH >= box.realY + box.hotY and self.realY + self.hotY <= box.realY + box.hotH + box.hotY
		
		if not (self.realX + self.hotX + self.hotW) >= (box.realX + box.hotX):
			return False
		if not (self.realX + self.hotX) <= (box.realX + box.hotW + box.hotX):
			return False
		if not (self.realY + self.hotY + self.hotH) >= (box.realY + box.hotY):
			return False
		if not (self.realY + self.hotY) <= (box.realY + box.hotH + box.hotY):
			return False
		return True
'''
	def CollidesWithAt (self, box):
		x_hits = self.realX + self.hotX + self.hotW >= box.realX and self.realX + self.hotX <= box.realX + box.hotW
		y_hits = self.realY + self.hotY + self.hotH >= box.realY and self.realY + self.hotY <= box.realY + box.hotH
		
		if x_hits is False or y_hits is False:
			return 'none'
		if self.realY + self.hotY + self.hotH >= box.realY and self.realY + self.hotY < box.realY:
			if x_hits:
				return 'bottom'
		if x_hits and y_hits:
			return 'other'
		if self.realX + self.hotX == box.realX + box.hotW or box.realX == self.realX + self.hotX + self.hotW:
			return 'on edge'
		return 'none'
	
	def CollidesWithHollowAt(self, hollow):
		return hollow.CollidesWith(self)
	
	def __str__(self):
		out = '<Box Object:: realHotX: %i realHotY: %i hotW: %i hotH: %i>' % (self.realX + self.hotX, self.realY + self.hotY, self.hotW, self.hotH)
		return out
	
class HollowBox(Box):
	def __init__(self, realX, realY, width, height):
		Box.__init__(self, realX, realY, width, height)
		self.left_edge = self.realX + self.hotX
		self.right_edge = self.realX + self.hotX + self.hotW
		self.top_edge = self.realY + self.hotY
		self.bottom_edge = self.realY + self.hotY + self.hotH
	
	##Warning, this WILL NOT test if it is actually on the line.
	##For that, I need to add restrictions to ends of edges 
	##(ie. the box's lines extend beyond the actual box)
	def CollidesWith(self, box):
		#Returns a boolean evaluation of whether this box's *edges*
		#collides with the box object passed
		
		if (self.left_edge >= box.realX
					and self.left_edge <= box.realX + box.hotW):
			return 'left'
		elif (self.right_edge >= box.realX
					and self.right_edge <= box.realX + box.hotW):
			return 'right'
		elif (self.top_edge >= box.realY
					and self.top_edge <= box.realY + box.hotH):
			return 'top'
		elif (self.bottom_edge >= box.realY
					and self.bottom_edge <= box.realY + box.hotH):
			return 'bottom'
		return 'none'
		
def CollidesWithHollowSides(box, hollow):
	if (hollow.left_edge >= box.realX
				and hollow.left_edge <= box.realX + box.hotW):
		return True
	elif (hollow.right_edge >= box.realX
				and hollow.right_edge <= box.realX + box.hotW):
		return True
	return False
	
def CollidesWithHollowBottom(solid, hollow):
	if (hollow.bottom_edge >= solid.realY
				and hollow.bottom_edge <= solid.realY + solid.height):
		return True
	return False
		
def DetectCollision (box1, box2):
	"Returns a boolean evaluation of whether two boxes collide"
	if (box1.realX  + box1.width >= box2.realX
		and box1.realX <= box2.realX + box2.width
		and box1.realY + box1.height >= box2.realY
		and box1.realY <= box2.realY + box2.height):
			return True
	return False
	
'''