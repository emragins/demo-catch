
import utility #(for translating pixel to tile)
from data import data

"""
object: whatever (player, enemy, block, etc.)
iheretance order: object -> moving entity -> entity -> box.  Box has realX/Y, hotX/Y/W/H
	or object -> entity -> box for objects which defy gravity yet still need to be solid
"""

def CheckSolidCollisionsForGravity(obj):
	if hasattr(obj.lastGravityCollision, 'realX'):	#if not None or a wall...
		if obj.CollidesWith(obj.lastGravityCollision):
			return obj.lastGravityCollision
	wallCollision = CheckCollisionsWalls(obj)
	if wallCollision: 
		return wallCollision
	return None

def CheckSolidCollisionsForMovement(obj):
	mapEdgeCollision = CheckCollisionsMapEdges(obj)	#if this gets moved after wallCollision, can end up out of bounds
	if mapEdgeCollision:
		return mapEdgeCollision
	wallCollision = CheckCollisionsWalls(obj)
	if wallCollision: 
		return wallCollision
	return None
	
def CheckCollisionsBalls(obj):
	for obj2 in data.objects:
		if hasattr(obj2, 'IsHeld'):	#denotes a ball
			if not obj2.IsHeld():
				if obj.CollidesWith(obj2):
					return obj2
	return None
	
def CheckCollisionsMapEdges(obj):
	if obj.realX + obj.hotX <= 0:
		return True
	if obj.realX + obj.hotX + obj.hotW  > data.map.NumPixelsWide():
		return True
	if obj.realY + obj.hotH > data.map.NumPixelsHigh(): ##non-movable map
		return True
	if obj.realY < 0:
		return False
	return False
	##purposely left out checking top of screen

def CheckCollisionsWalls(obj):
		
		"""
	This works in the following way:
	Corners of hotspot are tested:
		The map/tile realX's and realY's are established first, and tested immediately to maybe spare about 10 lines of code.
			This is seen in topleft and topright.
		Then the other two corners are tested.
	Sides of hotspot tested:
		Premise: if corner tiles are established, and there is a gap between these tiles, then these gaps are in the hotspot
		Test gaps on sides with variable realY (do this first since more sprites are taller than they are wide)
		Test gaps on top and bottom.
	Return True as soon as possible in order to save code.
	
	**Consider moving the 'guts' portion into its own function that would accept bounds and layer as args.**
	
	Note: This also only works for tiles that are 100% obstructed (or effectively so.)
		"""
		map = data.map
		
		hotx, hoty, hotw, hoth = obj.hotX, obj.hotY, obj.hotW, obj.hotH
		
		#bottomright (and establish bounds)
		RtileX, BtileY = utility.PixelToTile(obj.realX + hotx + hotw, obj.realY + hoty + hoth)
		obs = map.GetObs(RtileX, BtileY)
		if obs:
			return 'wall'	
		#topleft (and establish bounds)
		LtileX, TtileY = utility.PixelToTile(obj.realX + hotx, obj.realY + hoty)
		obs = map.GetObs(LtileX, TtileY)
		if obs:
			return 'wall'
		#topright
		obs = map.GetObs(RtileX, TtileY)
		if obs:
			return 'wall'
		#bottomleft
		obs = map.GetObs(LtileX, BtileY)
		if obs:
			return 'wall'
			
		#check to see if any gaps between tiles
		dx = RtileX - LtileX
		dy = BtileY - TtileY
		
		##next section mostly untested
		for i in range(dy-1): #aka, while dy > 1
			#left
			obs = map.GetObs(LtileX, TtileY + (i+1))
			if obs:
				return 'wall'
			#right
			obs = map.GetObs(RtileX, TtileY + (i+1))
			if obs:
				return 'wall'
				
		for i in range(dx-1): #aka, while dx > 1
			#top
			obs = map.GetObs(LtileX + (i+1), TtileY)
			if obs:
				return 'wall'
			#bottom
			obs = map.GetObs(LtileX + (i+1), BtileY)
			if obs:
				return 'wall'
				
		return None
