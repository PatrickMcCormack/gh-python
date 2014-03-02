#!/usr/bin/env python

#
# 4 Color Mapper
#

import pdb

# The map contains 7 states, the elements of the array called map. Each state is bordered by other states
# represented by the array at each state position in the map array.
# For example state 0 is bordered by states 1,4,2 and 5.
map 	  = [ [1,4,2,5], [0,4,6,5], [0,4,3,6,5], [2,4,6], [0,1,6,3,2], [2,6,1,0], [2,3,4,1,5] ]
mapcolors = [ None ] * len(map)
colors 	  = [ 'RED', 'YELLOW', 'GREEN', 'BLUE' ]

def check_color(color, connections):
	for i in connections:
		if color == mapcolors[i]:
			return False
	return True

def color_map(tile):
	if tile >= len(mapcolors):
		return True
	for color in colors:
		print color, '\t',  mapcolors
		if check_color(color, map[tile]):
			mapcolors[tile]=color
			if color_map(tile+1):
				return True
#		pdb.set_trace()
	return False

# Set the color of the first tile
print color_map(0)
print mapcolors

