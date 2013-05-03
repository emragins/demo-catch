from data import data
#import math #needed for floor'

#Needed to draw correctly to take into account camera movement
def MapToScreen(x, y):
	x -= data.map.NumPixelsWide()
	y -= data.map.NumPixelsHigh()
	return x, y
'''
def ScreenToMap(x, y):
	x += ika.Map.xwin
	y += ika.Map.ywin
	return x, y
'''
'''
which is more efficient??
floor - only uses 1 line, but unknown code number of operations behind it
iterate - min: 1, max: number of tiles in map direction. for right edges of a large map, could be a lot.
so guessing iterate probably for smaller maps, floor for bigger
'''

def PixelToTile(x, y):	
	#x = int(math.floor(x/ika.Map.tilewidth))
	#y = int(math.floor(y/ika.Map.tileheight))
	
	i = 0
	
	while x > i*data.map.TileSize():
		i+=1
	
	x = i-1	
	i = 0	
		
	while y > i*data.map.TileSize():
		i+=1
		
	y = i-1
	
	return x, y
	