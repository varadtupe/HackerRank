#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    count = 0
    for i in range(len(ar)-1):
        if i < len(ar)-1:
            for j in range(i+1,len(ar)):
                #print(i,j)
                if ((int(ar[i]) + int(ar[j])) % k == 0):
                    count += 1
    return count
                
            

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)

