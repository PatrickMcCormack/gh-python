#!/usr/bin/env python 

#
# compact_nqueens.py - basic backtracking nqueens solution
#

import sys
boardsize=8
recursive_calls=0

def print_solution(solution):
	for row in range(boardsize):
		column = solution[row]
		for i in range(boardsize):
			if i == column:
				sys.stdout.write('Q')
			else:
				sys.stdout.write('.')
		print

def queen_safe(r1,c1, solution):
	for r2 in range(len(solution)):
		c2 = solution[r2]
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
		if queen_safe(row, column, solution):
			solution.append(column) 
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
