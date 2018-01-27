def array_left_rotation(a, n, k):
    front = a[k:]
    back = a[:k]
    final = front + back
    return final
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

