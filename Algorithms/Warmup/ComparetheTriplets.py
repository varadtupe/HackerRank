
#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    score = [0,0]
    score = compare(a0,b0,score)
    score = compare(a1,b1,score)
    score = compare(a2,b2,score)
    return tuple(score)

def compare(inp1,inp2,score):
    if inp1 < inp2:
        score[1] += 1
    elif inp1 > inp2:
        score[0] += 1
    else:
        pass
    return score

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))



