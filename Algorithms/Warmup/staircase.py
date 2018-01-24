#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    for i in range(1,n):
        print(' ' * (n-1-i),'#'*i)
    print('#'*n)
    
    

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)

