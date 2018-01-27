#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    cnt = {}
    for i in ar:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    #print(cnt)
    mnCnt = 0
    for i in cnt:
        mnCnt += cnt[i]//2
    return mnCnt

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)

