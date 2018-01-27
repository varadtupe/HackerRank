def ransom_note(magazine, ransom):
    ranMap = {}
    #print(magazine)
    #print(ransom)
    for i in ransom:
        if i not in ranMap:
            ranMap[i] = 1
        else:
            ranMap[i] += 1
    #print(ranMap)
    for i in magazine:
        if i in ranMap and ranMap[i] > 0:
            ranMap[i] -= 1
            if ranMap[i] == 0:
                del(ranMap[i])
    
    if ranMap == {}:
        return True
    else:
        return False
            
            
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

