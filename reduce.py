#!/usr/bin/env python
#reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy

#number of columns of A/rows of B
n = int(sys.argv[1])

arr_a = {}
arr_b = {}
sum = 0.0
for i in range(0,n):
        arr_a[i] = 0.0
        arr_b[i] = 0.0

currentkey = None

for line in sys.stdin:
        line = line.strip()
        key_initial, value_initial = line.split('\t',1)
        key = key_initial.split(" ")
        value = value_initial.split(" ")


        if (value[0] == "A"):
                arr_a[int(value[1])] = float(value[2])
               

        if (value[0] == "B"):
                arr_b[int(value[1])] = float(value[2])


        #If we are still on the same key...
        if key_initial==currentkey:
                #Process key/value pair (your code goes here)
                sum = 0.0
                for i in range (0,n):
                        sum += arr_a[i] * arr_b[i]


        #Otherwise, if this is a new key...
        else:
                #If this is a new key and not the first key we've seen
                if currentkey:
                        #compute/output result to STDOUT (your code goes here)
			currentkey1, currentkey2 = currentkey.split(" ")
                        print '(%s, %s), %f' %(currentkey1,currentkey2,float(sum))
                        for i in range(0,n):
                                arr_a[i] = 0.0
                                arr_b[i] = 0.0

                        if (value[0] == "A"):
                                arr_a[int(value[1])] = float(value[2])
                                

                        if (value[0] == "B"):
                                arr_b[int(value[1])] = float(value[2])
                                

                currentkey = key_initial
                #Process input for new key (your code goes here)
                sum = 0.0

#Compute/output result for the last key (your code goes here)
if currentkey == key_initial:
	currentkey1, currentkey2 = currentkey.split(" ")
        print '(%s, %s), %f' %(currentkey1,currentkey2,float(sum))
        
