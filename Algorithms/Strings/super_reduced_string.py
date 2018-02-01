#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    stk = []
    for i in s:
        lenStk = len(stk)
        if lenStk == 0:
            stk.append(i)
        elif stk[lenStk-1] == i:
            del(stk[lenStk-1])
        else:
            stk.append(i)
    if len(stk) == 0:
        return 'Empty String'
    else:
        return ''.join(stk)
    
s = input().strip()
result = super_reduced_string(s)
print(result)

