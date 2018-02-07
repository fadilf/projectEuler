#	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#	Find the sum of all the multiples of 3 or 5 below 1000.

max = 1000
x = 0
for i in range(3,max,3):
	if i%5 != 0:
		x += i
for i in range(5,max,5):
	x += i

print x