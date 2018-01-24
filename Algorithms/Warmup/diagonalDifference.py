#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    dim = len(a[1])
    l_diag, r_diag = 0,0
    for i in range(dim):
        l_diag += a[i][i]
        r_diag += a[i][dim-1-i]
    
    return abs(l_diag - r_diag)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)

