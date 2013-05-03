import ika


"""
NOTE: This map is meant for one layer, one type of tile, and all tiles 100% obstructed.
"""

class GameMap(object):
	def __init__(self, widthInPixels, heightInPixels, tileSize):
		self.map = self.GenerateMap(widthInPixels, heightInPixels, tileSize)
		self.tileImage = ika.Image("images\\tile1.png")
		self.widthInPixels = widthInPixels
		self.heightInPixels = heightInPixels
		self.tileSize = tileSize
		
	def Update(self):
		pass
		
	def Render(self):
		for i in range(self.tilesHigh):
			y_pos = i*self.tileSize
			for j in range(self.tilesWide):
				if self.map[i][j] is 1:
					ika.Video.Blit(self.tileImage, j*self.tileSize, y_pos)
	
	def GetObs(self, x_tile, y_tile):
		return self.map[y_tile][x_tile]

	def NumTilesWide(self):
		return self.tilesWide
	def NumTilesHigh(self):
		return self.tilesHigh
	def NumPixelsWide(self):
		return self.widthInPixels
	def NumPixelsHigh(self):
		return self.heightInPixels
	def TileSize(self):
		return self.tileSize
		
	##assumes tiles will fit evenly into picture
	def GenerateMap(self, widthInPixels, heightInPixels, tileSize):
		self.tilesWide = int(widthInPixels / tileSize)
		self.tilesHigh = int(heightInPixels / tileSize)
	
		#make initial flat land
		maxFloorHeight = int(self.tilesHigh/3)
		baseFloorHeight = int(2*self.tilesHigh/3)
		map = []
		for i in range(self.tilesHigh):
			if i < baseFloorHeight:
				map.append([0 for j in range(self.tilesWide)])
			else:
				map.append([1 for j in range(self.tilesWide)])
			
		#adjust to not be so flat
		# idea - make an adjuster that goes through one column at a time and will either rise or fall with each column
		adjHeight = baseFloorHeight 
		for i in range(self.tilesWide):
			adjHeight += ika.Random(-1,2)
			if adjHeight > self.tilesHigh - maxFloorHeight:
				adjHeight = self.tilesHigh - maxFloorHeight
			elif adjHeight < maxFloorHeight:
				adjHeight = maxFloorHeight
			dif = adjHeight - baseFloorHeight
			if dif < 0:
				while dif < 0:
					map[baseFloorHeight + dif][i] = 1
					dif += 1
			elif dif > 0:
				while dif >= 0:
					map[baseFloorHeight + dif][i] = 0
					dif -= 1
			else:
				map[baseFloorHeight][i] = ika.Random(0,2)
				
		return map
			
		
		