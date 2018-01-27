pB = {}
n = int(input())
for _ in range(n):
    inp = input()
    inp = inp.split(' ')
    pB[inp[0]] = int(inp[1])

for _ in range(n):
    inp = input()
    if inp in pB:
        print("".join(map(str,[inp,'=',pB[inp]])))
    else:
        print('Not found')
        



