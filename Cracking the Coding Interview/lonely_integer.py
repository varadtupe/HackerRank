#!/bin/python3

import sys

def lonely_integer(a):
    keyDict = {}
    for i in a:
        if i in keyDict:
            del(keyDict[i])
        else:
            keyDict[i] = 1
    res = list(keyDict.keys())
    return(res[0])        
            
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

