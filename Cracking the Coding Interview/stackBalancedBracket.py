def is_matched(expression):
    bkDict = {'{':'}','[':']','(':')'}
    bkStack = []
    for i in expression:
        if bkDict.get(i):
            bkStack.append(bkDict[i])
        else:
            if len(bkStack) == 0 or i != bkStack[len(bkStack)-1]:
                return False
            bkStack.pop()
    if len(bkStack) == 0:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

