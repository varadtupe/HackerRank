#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    sum_list = []
    for i in range(len(arr)):
        arr_copy = arr.copy()
        del arr_copy[i]
        sum_list.append(sum(arr_copy))
    print (min(sum_list),max(sum_list))


if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)

