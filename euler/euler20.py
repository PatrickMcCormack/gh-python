#!/usr/bin/env python

import math

def num_digits(num):
	nd = 0
	while num > 1:
		num = num / 10
		nd = nd + 1
	return nd

def num_to_array(num):
	digits = []
	power = num_digits(num) - 1
	for position in range(power, 0, -1):
		tens = 10 ** (position)
		digit = math.floor(num / tens)
		digits.append(digit)
		num = num - (digit * tens)
	digits.append(num)
	return digits

print('projecteuler.net, problem 20')

num = math.factorial(100)

num_array = num_to_array(num)

print(num)
print(num_array)

total=0
for s in num_array:
	total += s

print(total)


