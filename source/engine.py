
from manager import manager
import ika
last_fps = 0


def MainLoop():
	last_update = 0
	
	while 1:
		if ika.GetTime() > last_update + 1:
			last_update = ika.GetTime()            

			global last_fps

			if last_fps != ika.GetFrameRate():
				ika.SetCaption( str("Demo by Eve Ragins    FPS(" + str(last_fps) + ")"))
				last_fps = ika.GetFrameRate()

			ika.Input.Update()
			manager.Update()
			
			last_update = ika.GetTime()+1
			
			
		##will need to remove this when outputting map layer by layer in Manager	
		#ika.Render()	#map
		
		manager.Render()
		
		
		ika.Video.ShowPage()
		
def NewGame():
	import map
	import player
	import ball
	import ballmech
	from data import data
	
	data.ClearAll()
	data.AssignMap(map.GameMap(400,320,16))
	data.AssignPlayer(player.Player(16*5, 16*4))
	data.AddObject(ball.Ball(150,100))
	data.AddObject(ballmech.BallMech(300,100))
	

