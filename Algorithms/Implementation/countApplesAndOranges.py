#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    abs_apples = [x+a for x in apples]
    abs_oranges = [x+b for x in oranges]
    #print(abs_apples,abs_oranges)
    app = len(([i for i in abs_apples if i>=s and i <=t]))
    org = len(([i for i in abs_oranges if i>=s and i <=t]))
    print(app)
    print(org)

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)

