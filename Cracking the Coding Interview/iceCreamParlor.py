#!/bin/python3

import sys

def solve(arr, money):
    # Complete this function
    costMap = {}
    for i in range(len(arr)):
        cst = arr[i]
        if cst in costMap:
            costMap[cst] += [i+1]
        else:
            costMap[cst] = [i+1]
    for i in costMap:
        if money-i in costMap:
            if money-i == i:
                print(costMap[i][0],costMap[i][1])
                break
            else:
                print(costMap[i][0],costMap[money-i][0])
                break
    
       

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)

