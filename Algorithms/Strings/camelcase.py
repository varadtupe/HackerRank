#!/bin/python3

import sys

def camelcase(s):
    # Complete this function
    laststore = 0
    res = []
    for i in range(len(s)):
        char = s[i]
        if char.isupper():    
            res += [s[laststore:i]]
            laststore = i
        if i == len(s)-1:
            res += [s[laststore:]]
    return len(res)
if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)

