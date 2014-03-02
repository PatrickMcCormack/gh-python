#!/usr/bin/env python
#

# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

print('projecteuler.net, problem 9')

import math

for a in range(1,1001):
	for b in range(1,1001):
		for c in range(1,1001):
			if ((a ** 2) + (b ** 2)) == (c ** 2):
				if a < b < c:
					if a + b + c == 1000:
						product = a * b * c
						print('{0} {1} {2} : product = {3}'.format(a,b,c,product))


