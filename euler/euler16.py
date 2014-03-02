#!/usr/bin/env python
#
# What is the sum of the digits of the number 2^1000

import math

print('projecteuler.net, problem 16')

n = 2 ** 1000
s = str(n)

sum = 0
for i in s:
	sum += int(i)

print(sum)


