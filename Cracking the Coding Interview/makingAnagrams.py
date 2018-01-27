def number_needed(a, b):
    dictWord = {}
    for i in a:
        if i not in dictWord:
            dictWord[i] = 1
        else:
            dictWord[i] += 1
    for i in b:
        if i not in dictWord:
            dictWord[i] = -1
        else:
            dictWord[i] -= 1
    #print(dictWord)
    num = 0
    for i in dictWord:
        num += abs(dictWord[i])
    return num

a = input().strip()
b = input().strip()

print(number_needed(a, b))

