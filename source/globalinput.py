import ika
from data import data
import map
import ball

class GlobalInput(object):
	def __init__(self):
		self.displayInstructions = True
		self.font = ika.Font('fonts\\ocr_green.fnt')
		
		self.list = ['F1: \t\t\t\t Toggle Instructions', 
				'PageUp/Down: \t Y Velocity',
				'Home/End: \t\t X Velocity',
				'Space: \t\t\t Throw',
				'Arrow Keys: \t\t Move',
				'F5: \t\t\t\t Reset with new map',
				'F6: \t\t\t\t Make new ball',
				'F7: \t\t\t\t Clear all balls']
		
	def Update(self):
		kb = ika.Input.keyboard
		
		if kb['F1'].Pressed():
			if self.displayInstructions:
				self.displayInstructions = False
			else:
				self.displayInstructions = True
				
		if kb['F5'].Pressed():
			import engine
			engine.NewGame()
			
		if kb['F6'].Pressed():
			x = ika.Random(0,390)
			newball = ball.Ball(x, 0)
			data.objects.append(newball)
		
		if kb['F7'].Pressed():
			#clear the screen of all balls
			self.ClearScreen()
			
		
	def Render(self):
		if self.displayInstructions:
			ika.Video.DrawRect(0,0,400,320,ika.RGB(25,25,25),1)
			
			for i, string in enumerate(self.list):
				self.font.Print(10, (i+1)*25, string)
			
	def ClearScreen(self):
		##should be a better way to do this
		list = []
		for i, obj in enumerate(data.objects):
			if hasattr(obj, 'IsThrown'):
				list.append(i)
		for i in reversed(list):
			data.objects.pop(i)
			
			