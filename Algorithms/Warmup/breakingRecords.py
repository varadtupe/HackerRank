#!/bin/python3

import sys

def breakingRecords(score):
    # Complete this function
    highCount = 0
    lowCount = 0
    maxSc,minSc = score[0],score[0]
    blank = []
    for i in score:
        blank.append(i)
        #print(blank)
        blankMaxSc = max(blank)
        blankMinSc = min(blank)
        #print(maxSc,blankMaxSc,minSc,blankMinSc)
        if blankMaxSc > maxSc:
            highCount += 1
            maxSc = blankMaxSc
            #print('high', highCount,maxSc)
        if blankMinSc < minSc:

            lowCount += 1
            minSc = blankMinSc
            #print('low',lowCount,minSc)
    return [highCount,lowCount]


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))



