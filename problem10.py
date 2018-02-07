#	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#	Find the sum of all the primes below two million.

primes = 1
sum = 2
i = 2
#print 2
while i < 2*10**6:
	i += 1
	for j in range(2,i):
		if i%j == 0:
			break
		if i%j != 0 and j == i-1:
			primes += 1
#			print i
			sum += i

print "Sum of primes:"
print sum