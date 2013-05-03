
class Data(object):
	def __init__(self):
		self.objects = []
		self.player = None
		self.map = None	
			
	def AddObject(self, obj):
		self.objects.append(obj)

	def AddPassive(self, obj):
		self.passives.append(obj)
	
	def AssignPlayer(self, obj):
		self.player = obj
	
	def AssignMap(self, obj):
		self.map = obj
	
	def ClearAll(self):
		self.objects = []
		self.player = None
		self.map = None	
	
	
data = Data()