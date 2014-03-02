#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3.2
#
# A palindromic number reads the same both ways. The largest palindrome made 
#  from the product of two 2-digit numbers is 9009 = 91  99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def num_digits(num):
	nd = 0
	while num > 1:
		num = num / 10
		nd = nd + 1
	return nd

def palindrome(numbers):
	numbers2 = numbers[::-1]
	result  = True
	for i in range(len(numbers)):
		if numbers[i] != numbers2[i]:
			result = False
			break
	return result

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

maxnum = 0

for o in range(999, 0, -1):
	for i in range(999, 0, -1):
		num = o * i
		digits = num_to_array(num)
		if palindrome(digits) == True:
			if maxnum < num:
				maxnum = num

print('maxnum = {0}'.format(maxnum))




