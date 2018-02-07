#	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def prime_factors(number):
	array = {
		1: 1
	}
	i = 2
	while(number != 1):
		if number%i == 0:
			if(i in array):
				array[i] += 1
			else:
				array[i] = 1
			number /= i
		else:
			i += 1
	return array
max = 20
factors = {}
for i in range(1,max+1):
	temp = prime_factors(i)
	for factor in temp:
		if factor in factors:
			if factors[factor] <= temp[factor]:
				factors[factor] = temp[factor]
		else:
			factors[factor] = temp[factor]
answer = 1
for factor in factors:
	answer *= factor**factors[factor]
print answer