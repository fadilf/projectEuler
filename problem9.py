#	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#	a2 + b2 = c2
#
#	For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#	Find the product abc.

import math
import sys

for a in range(1,333):
	for b in range(a,666):
		c = 1000 - a - b
		if c != math.sqrt(a**2 + b**2):
			continue
		else:
			print a * b * c
			sys.exit()