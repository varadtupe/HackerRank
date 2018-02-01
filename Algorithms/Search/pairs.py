#!/bin/python3

import sys

def pairs(k, arr):
    # Complete this function
    #print(k)
    #print(arr)
    #old code works slow for some test cases
    '''a=list(set(arr))
    cnt = 0
    for i in range(len(a)):
        sub = a[i+1:]
        cur = a[i]
        for j in sub:            
            if abs(cur-j) == k:
                cnt += 1
    return cnt    '''
    
    #using set theory
    cnt = len(set(arr) & set(x + k for x in arr))
    return cnt

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)

