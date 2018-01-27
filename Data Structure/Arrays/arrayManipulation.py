#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    ml = [0] * n    
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        #print(ml)
        for i in range(a-1,b):
            ml[i] +=  k
    print(max(ml))

    
    