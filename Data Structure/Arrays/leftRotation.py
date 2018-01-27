#!/bin/python3

import sys

def leftRotation(a, d):
    # Complete this function
    front = a[d:]
    back = a[:d]
    final = front + back
    return final

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))



