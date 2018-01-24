#!/bin/python3

import sys
def plusMinus(arr):
    # Complete this function
    arr_len = len(arr)
    if arr_len > 0:
        arr_len = float(arr_len)
        counter = [0,0,0]
        for i in arr:
            if i > 0:
                counter[0] += 1
            elif i<0:
                counter[1] += 1
            else:
                counter[2] += 1
        print(counter[0]/arr_len)
        print(counter[1]/arr_len)
        print(counter[2]/arr_len)        


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)

