#	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#	What is the 10 001st prime number?

primes = 1
i = 2
while primes < 10001:
	i += 1
	for j in range(2,i):
		if i%j == 0:
			break
		if i%j != 0 and j == i-1:
			primes += 1
			print i
			print primes

print i
print primes