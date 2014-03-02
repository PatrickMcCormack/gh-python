#!/usr/bin/env python

import math

print('projecteuler.net, problem 6')

sum_squares = 0
square_sum = 0
for i in range(1,101):
	sum_squares = sum_squares + i ** 2
	square_sum = square_sum + i

square_sum = square_sum ** 2

print('sum of squares  = {0}'.format(sum_squares))
print('square of sumes = {0}'.format(square_sum))
print('square of sumes = {0}'.format(square_sum - sum_squares))

