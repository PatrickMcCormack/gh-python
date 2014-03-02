#!/usr/bin/env python 

#
# ir_nqueens.py - iterative repair n queens solution
#

import sys, random
boardsize=20
iterations=0

def print_solution(solution):
	for row in range(boardsize):
		column = solution[row]
		for i in range(boardsize):
			if i == column:
				sys.stdout.write('Q')
			else:
				sys.stdout.write('.')
		print

def score_position(r1,c1):
	aggressors=0
	for r2 in range(len(solution)):
		c2 = solution[r2]
		if r1 != r2:
			if c1 == c2:
				aggressors+=1
			else:
				slope = abs(float((float(r1) - float(r2)) / (float(c1) - float(c2))))
				if slope == 1:
					aggressors+=1
	return aggressors

def score_board(solution):
	score=[]
	for r1 in range(len(solution)):
		c1 = solution[r1]
		score.append(score_position(r1,c1))	
	return score

def optimize_board(solution):
	global iterations
	iterations += 1
	score = score_board(solution)
	m = max(score)
	if m == 0:
		return True
	l = random.randint(1,score.count(m))
	row = 0
	for i in range(len(score)):
		if score[i] == m:
			l -= 1
			if l == 0:
				row = i	
				break
	# this is a really dumb way of repairing the board, it picks a random new position
	# but this is amazingly efficient, orders of magnitude faster than just brute force
	# backtracking.
	solution[row] = random.randint(0,boardsize-1)
	return False

# main

print "\nnqueens implemented using iterative repair\n"
# Initialize the solution by putting each queen diagonally on the board
solution = [i for i in range(boardsize)]
print solution
while 1 == 1:
	optimized = optimize_board(solution)
	if optimized == True:
		break
print "Iterations = ", iterations
print_solution(solution)
print solution
print
