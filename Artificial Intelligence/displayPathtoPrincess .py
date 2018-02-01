#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    #print(n)
    #print(grid)
    pri = []
    mot = []
    for i in range(n):
        #print(grid[i])
        tmp = grid[i]
        #print(tmp)
        if 'p' in tmp:
            pri.append(i)
            pri.append(tmp.index('p'))
        if 'm' in tmp:
            mot.append(i)
            mot.append(tmp.index('m'))
    #print(mot,pri)        
    hor = mot[0]-pri[0]
    ver = mot[1]-pri[1]
    if hor >= 0:
        horDir = 'LEFT'
    else:
        hor = abs(hor)
        horDir = 'RIGHT'
    for i in range(hor):
        print(horDir)
    if ver >= 0:
        verDir = 'UP'
    else:
        ver=abs(ver)
        verDir = 'DOWN'
    for i in range(ver):
        print(verDir)
            

        
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
    


