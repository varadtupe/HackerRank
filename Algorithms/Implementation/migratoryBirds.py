#!/bin/python3

import sys
def migratoryBirds(n, ar):
    # Complete this function
    cnts = [0]*n
    for i in ar:
        cnts[i-1] += 1
#    print(max(cnts))    
    return cnts.index(max(cnts))+1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

