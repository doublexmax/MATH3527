#!/usr/bin/env python3

import sys

def main():
	decimal_len = int(sys.argv[1])

	if len(sys.argv) > 2:
		prime_limit = int(sys.argv[2])
	else:
		prime_limit = 10000

	print(primes_with_period(decimal_len, limit = prime_limit))

def run_primes(n):
	primes = []

	for i in range(2, n + 1):
		is_prime = True
		for prime in primes:
			if i % prime == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(i)

	return primes

def primes_with_period(x, limit):
	primes = run_primes(limit)

	valid = []

	for prime in primes:
		if (10**x - 1) % prime == 0:
			valid.append(prime)
	
	return valid

if __name__ == '__main__':
	main()
