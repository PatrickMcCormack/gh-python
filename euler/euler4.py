#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3.2
#
# A palindromic number reads the same both ways. The largest palindrome made 
#  from the product of two 2-digit numbers is 9009 = 91  99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

maxnum = 0

for o in range(999, 0, -1):
	for i in range(999, 0, -1):
		num = o * i
		s = str(num)
		if s == s[::-1]:
			if maxnum < num:
				maxnum = num

print('maxnum = {0}'.format(maxnum))




