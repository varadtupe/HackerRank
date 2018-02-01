s = int(input().strip())
dict = {0:0, 1:1, 2:2, 3:4}

def steps(n):
    if n in dict.keys():
        return dict.get(n)
    result = steps(n-3) + steps(n-2) + steps(n-1)
    dict.update({n: result})
    return dict.get(n)

for a0 in range(s):
    n = int(input().strip())
    print(steps(n))
    
    

