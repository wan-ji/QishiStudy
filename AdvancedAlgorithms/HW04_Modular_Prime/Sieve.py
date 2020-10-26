'''
Simple Sieve
Segmented Sieve
'''
import math


def simpleSieve(n):
	if n <= 1:
		return []

	isPrime = [True] * (n+1)
	isPrime[0] = isPrime[1] = False

	for i in range(2, math.floor(math.sqrt(n))+1):
		if isPrime[i]:
			for j in range(i*i, n+1, i):
				isPrime[j] = False

	return [i for i in range(n+1) if isPrime[i]]


def segmentedSieve(n):
	if n <= 1:
		return []

	m = int(math.floor(math.sqrt(n)))
	primes = simpleSieve(m)

	ans = [] + primes


	for low in range(m+1, n+1, m):
		high = min(low + m - 1, n)
		isPrime = [True] * (m + 1)

		for prime in primes:
			for j in range(math.ceil(low/prime), math.floor(high/prime) + 1):
				isPrime[prime*j - low] = False

		for i in range(low, high + 1):
			if isPrime[i-low]:
				ans.append(i)

	return ans






def test():

	print(simpleSieve(53))
	print(segmentedSieve(53))




test()

