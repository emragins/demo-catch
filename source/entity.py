
import ika

import box
	
class Entity(box.Box):
	def __init__(self, x, y, type):
		#hot coordinates are relative to x/y position
		self.hotX = 0
		self.hotY = 0
		self.hotW = 0
		self.hotH = 0
		
		self.GetAndSetImageData(type)
		
		self.dead = False
		self.realX = x
		self.realY = y
		
		box.Box.__init__(self, self.realX, self.realY, self.hotX, self.hotY, self.hotW, self.hotH)
		
		
	def Update(self):
		pass
		
	def Render(self):
		pass ##
		
	def IsAlive(self):
		if self.dead == False:
			return True
		return False
	
	##bleh. fix.
	def GetAndSetImageData(self, type):
		import imagedata
		data = imagedata.GetImageData(type)
		self.hotX = data['hotX']
		self.hotY = data['hotY']
		self.hotW = data['hotW']
		self.hotH = data['hotH']