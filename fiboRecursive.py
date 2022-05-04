#!/bin/python3

def doRecursiveFibo(n):
	if n <= 1:
		return n
	else:
		return(doRecursiveFibo(n-1) + doRecursiveFibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
	print ("Plese enter a positive integer")
else:
	print ("Fibonacci sequence:")

for i in range(nterms):
	print (doRecursiveFibo(i))
