#
def nextMove(n,r,c,grid):
    pri = []
    mot = [r,c]
    flag = True
    for i in range(n):
        #print(grid[i])
        tmp = grid[i]
        #print(tmp)
        if 'p' in tmp:
            pri.append(i)
            pri.append(tmp.index('p'))
    #print(mot,pri)        
    
    ver = mot[0]-pri[0]
    hor = mot[1]-pri[1]
    #print(hor,ver)
    if hor > 0:
        horDir = 'LEFT'
    elif hor < 0:
        hor = abs(hor)
        horDir = 'RIGHT'
    else:
        flag = False
    if flag:
        op = horDir
        
    if ver > 0:
        verDir = 'UP'
    elif ver < 0:
        ver=abs(ver)
        verDir = 'DOWN'
    else:
        flag = False
    if flag:
        op = verDir
    return op
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

