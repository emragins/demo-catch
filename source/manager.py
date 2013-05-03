from data import data
import globalinput
"""
class to manage which order groups of things need to be updated and displayed
ie. player always comes last when being displayed

"""


##will have to add map specific with layers in correct order to render
class Manager:
	def __init__(self):
		self.g_input = globalinput.GlobalInput()
	def Update(self):
		data.player.Update()
		
		self.g_input.Update()
		
		for obj in data.objects:
			print 'updating object', obj
			obj.Update()
		
	def Render(self):
		data.map.Render()
		
		for obj in data.objects:
			obj.Render()
			
		data.player.Render()
		
		self.g_input.Render()	#for instructions
		
manager = Manager()
			
			