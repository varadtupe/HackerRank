import numpy as np
from scipy import stats

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    #print(n)
    #print(arr)
    print(np.mean(arr))
    print(np.median(arr))
    print(int(stats.mode(arr)[0]))


