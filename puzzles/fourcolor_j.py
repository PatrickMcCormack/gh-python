#!/usr/bin/env python

#
# 4 Color Mapper
#

map 	  = [ [1,4,2,5], [0,4,6,5], [0,4,3,6,5], [2,4,6], [0,1,6,3,2], [2,6,1,0], [2,3,4,1,5] ]
#map 	  = [ [1,2], [0,2], [0,1] ]
mapcolors = [ None ] * len(map)
colors 	  = [ 'RED', 'YELLOW', 'GREEN', 'BLUE' ]

def check_color(color, connections):
	for i in connections:
		if color == mapcolors[i]:
			return False
	return True

def color_map(tile, color):
	if tile >= len(mapcolors):
		return True
	print color, '\t', mapcolors
	if check_color(color, map[tile]):
		mapcolors[tile] = color	
		for c in colors:
			if color_map(tile+1, c):  # keep looping over explore until a color is found
				return True 
	return False # a color could not be found - stack will unwind and coloring has failed

# Set the color of the first tile
print color_map(0, 'RED')
print mapcolors
