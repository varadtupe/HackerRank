def getFibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return getFibonacci(n-1)+getFibonacci(n-2)


def fibonacci(n):
    # Write your code here.
    '''i=1
    lastNum = 0
    while lastNum < n:
        lastNum = getFibonacci(i)
        i +=1
    return lastNum'''
    n=n+1
    res = 0
    if n<0:
        print("Incorrect input")
    elif n==1:
        res = 0
    elif n==2:
        res = 1
    else:
        res =  getFibonacci(n-1)+getFibonacci(n-2)
    #print(n,res)
    return res


        
        

n = int(input())
print(fibonacci(n))

