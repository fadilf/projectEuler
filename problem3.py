#	The prime factors of 13195 are 5, 7, 13 and 29.
#
#	What is the largest prime factor of the number 600851475143 ?

number = 600851475143

hpf = 1
i = 1
while number !=1:
	if number%i == 0:
		hpf = i
		number /= i
	i += 1

print hpf