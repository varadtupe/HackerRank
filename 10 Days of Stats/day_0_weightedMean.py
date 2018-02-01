
if __name__ == "__main__":
    n = int(input().strip())
    X = list(map(int, input().strip().split(' ')))
    W = list(map(int, input().strip().split(' ')))
    ws = 0
    bs = 0
    for i in range(n):
        ws += X[i] * W[i]
        bs += W[i]
    print(round(ws/bs,1))    
        

