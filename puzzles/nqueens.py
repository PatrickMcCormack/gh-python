#!/usr/bin/env python 

#
# nqueens.py - basic backtracking nqueens solution
#
# this can be made more compact by removing the row numbers,
# the row's can be implicit with the soluion just being a 
# list of columns

import sys
boardsize=4
recursive_calls=0

def print_solution(solution):
	for row in range(boardsize):
		column = solution[row][1]
		for i in range(boardsize):
			if i == column:
				sys.stdout.write('Q')
			else:
				sys.stdout.write('.')
		print

def queen_safe(position, solution):
	r1 = position[0]
	c1 = position[1]
	for p in solution:
		r2 = p[0]
		c2 = p[1]
#		if (r1 == r2) or (c1==c2): 
		if c1==c2: 
			return False
		slope = abs(float((float(r1) - float(r2)) / (float(c1) - float(c2))))
		if slope == 1:
			return False
	return True

def place_queen(row, solution):
	global recursive_calls
	if row >= boardsize:
		return True
	recursive_calls += 1
	for column in range(boardsize):
		position = (row,column)
		if queen_safe(position, solution):
			solution.append(position) 
			if place_queen(row+1, solution):
				return True
			solution.pop() # backtrack by removing the last partial solution
	return False

# main

print "\nnqueens!\n"
solution = []
place_queen(0, solution)
print solution
print
print("recursive calls: " + str(recursive_calls))
print 
print_solution(solution)
print
