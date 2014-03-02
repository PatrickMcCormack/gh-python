#!/usr/bin/env python

#
# Solve Wolf, Sheep, Cabbage 
# 
# This is a simple puzzle that can be figured out in your head but 
# for fun I wanted to encode an solution.
#
# The algo is pretty simple:
#
#	move object from mainland to island. Check first if the object can
#       be moved, i.e. you cannot move the cabbage and leave the wolf and the 
#	sheep together.
#
#	If there is already an object on the island which clashes with the 
#	object in the boat, swap the contents of the boat with the object
#	on the island and move the object from the island to the mainland
#	repeat until everthing is moved to the island. 
# 

from collections import deque

mainland = deque([ 'cabbage', 'sheep', 'wolf' ])
island = []
boat = []

encoding = {
	'wolf':	   0b10,
	'cabbage': 0b10,
	'sheep':   0b01 
	}

#
# check which object can be moved from the mainland
#
def check_mainland():
	global mainland
	object = None
	# if there are two or one object on the mainland just move one 
	if len(mainland) <3:
		object = mainland.pop()
	else:
		# when there are 3 objects on the island move the one 
		# which can be moved without causing a conflict
		for i in range(len(mainland)):
			object = mainland.pop()
			tmp = 0
			for obj in mainland:
				tmp = tmp ^ encoding[obj]
			if tmp == 0:
				break
			else:
				mainland.appendleft(object)

	return object

#
# check if the item can move from the boat to the island
#
def check_island(boat):
	removed = None
	be = encoding[boat]
	for object in island:
		oe = encoding[object]
		if oe ^ be:
			removed = object
			break
	if removed is not None:
		island.remove(removed)
	return removed

#
# main
#

print('\nWolf, Cabbage, Sheep Puzzle\n')
		
while len(mainland) > 0:
	boat = check_mainland()
	print ('Putting ' + boat + ' into the boat')
	if len(mainland) == 0:
		print('Moving ' + boat + ' to island')
		island.append(boat)
		break
	object = check_island(boat)
	if object is not None:
		island.append(boat)
		mainland.appendleft(object)
		print('Swaping ' + boat + ' from boat to island and the ' + object + \
					' gets back in the boat and is moved to the mainland')
	else:
		island.append(boat)
		print('Moving ' + boat + ' to island')

print


