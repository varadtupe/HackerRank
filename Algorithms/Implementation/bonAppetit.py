#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    bill = ar.copy()
    del(bill[k])
    sumBill = sum(bill)
    split = int(sumBill/2)
    #print(split,b)
    if split >= b:
        return "Bon Appetit"
    else:
        return abs(split-b)
    

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)

