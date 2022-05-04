#!/bin/python3

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
	print ("Plese enter a positive integer")
else:
	print ("Array Fibonacci sequence:")

fiboAry = []
currentIdx = 0
for i in range(nterms):
	if currentIdx <= 1: 
		fiboAry.append(i) 
	else:
		fiboAry.append(fiboAry[currentIdx-2] + fiboAry[currentIdx-1])
	
	currentIdx += 1

for val in fiboAry:
	print(val)
	
