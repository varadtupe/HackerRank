#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        curr_grd = grades[i]
        if curr_grd >= 38 and curr_grd % 5 > 2:
            curr_grd += 5 - (curr_grd % 5)
            grades[i] = curr_grd
            

    return grades
    

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



