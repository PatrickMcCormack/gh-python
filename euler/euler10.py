#!/usr/bin/env python

import sys, math

def sieve(maxnum):
	primes = [-1 for x in range(maxnum)]
	primes[0] = 0
	primes[1] = 0  # don't count 1 as prime
	i = 2
	while (i < maxnum):
		if primes[i] == -1:
			for multiple in range(i, maxnum, i): 
				primes[multiple] = 0
			primes[i] = i
		i = i + 1
	primes = [x for x in primes if primes[x] != 0]
	return primes

print('projecteuler.net, problem 10')

bignum = 2000000
primes = sieve(bignum + 1)

print('num primes = {0}'.format(len(primes)))

prime_total=0
for i in primes:
	prime_total += i

print(' prime total = {0}'.format(prime_total))
