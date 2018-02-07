#	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
#	Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0;
for x in range(999,100,-1):
	for i in range(999,100,-1):
		product = i*x
		if product <= 10**5:
			break
		product = str(product)
		if product[3:] == product[2::-1]:
			if product > largest:
				largest = product
			break
print largest