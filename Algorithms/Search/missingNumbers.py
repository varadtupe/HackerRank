#!/bin/python3

import sys

def missingNumbers(arr, brr):
    # Complete this function
    brr_map = {}
    for i in brr:
        if i in brr_map:
            brr_map[i] +=1
        else:
            brr_map[i] =1
    
    for i in arr:
        if i in brr_map:
            brr_map[i] -=1
            if brr_map[i] == 0:
                del(brr_map[i])
                
    return sorted(brr_map.keys())

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))



