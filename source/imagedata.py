import frames

##LOOK IN UTILITY MODULE FOR IMAGE CACHE CODE... SHOULD USE IT WHEN STARTING TO GET OPTIONS

def GetImageData(type):
	if type is 'player':
		return player
	if type is 'ball':
		return ball
	if type is 'ballmech':
		return ballmech
	else:
		return Default() #really here to not break stuff
		
#def GetAnimationData(type):

def Player():
	image = "images\\hero.png"
	framelist = frames.LoadFrames(0,0,image,32,32,12)

	animations = {
		'MoveLeft': [0,1,0,2],
		'MoveRight': [5,7,6,7],
		'WaitLeft': [3], 
		'WaitRight': [4],
		'JumpLeft': [9], 
		'JumpRight': [8],
		'GrabLeft': [10],
		'GrabRight': [11],
		'FallLeft': [9],
		'FallRight': [8]
		}
	
	data = {
			'animations': animations,
			'frames': framelist,
			'hotX': 9,
			'hotY': 8, #not at 0 since head hits stuff too soon
			'hotW': 14,
			'hotH': 23,
			'width': 32,
			'height': 32	
			}
	
	return data

def Ball():
	image = "images\\ball.png"
	framelist = frames.LoadFrames(0,0,image,8,8,1)
	
	animations = {
		'MoveLeft': [0],
		'MoveRight': [0],
		'WaitLeft': [0], 
		'WaitRight': [0]
		}
	
	data = {
		'animations': animations,
		'frames': framelist,
		'hotX': 0,
		'hotY': 0, 
		'hotW': 7,
		'hotH': 7,
		'width': 8,
		'height': 8
		}
	
	return data
	
def BallMech():
	image = "images\\ballmech.png"
	framelist = frames.LoadFrames(0,0,image,16,16,6)
	
	animations = {
		'MoveLeft': [1],
		'MoveRight': [2],
		'WaitLeft': [0], 
		'WaitRight': [0],
		'HasBall': [4],
		'ThrowsLeft': [5,6],
		'ThrowsRight': [5,6]
		}
	
	data = {
		'animations': animations,
		'frames': framelist,
		'hotX': 1,
		'hotY': 0, 
		'hotW': 14,
		'hotH': 15,
		'width': 16,
		'height': 16
		}
	
	return data
	
def Default():
##need to change specifics for default
	image = "images\\hero.png"
	framelist = frames.LoadFrames(0,0,image,16,16,8)
	data = {
			'frames': framelist,
			'hotX': 1,
			'hotY': 1,
			'hotW': 15,
			'hotH': 15,
			'width': 16,
			'height': 16
			}
		
	return data
		

player = Player()
ball = Ball()
ballmech = BallMech()

		