def countOccur(q,inpStr):
    cnt = 0
    for i in inputStr:
        if i == q:
            cnt +=1
    return cnt

N = int(input())
inputStr = []
for i in range(N):
	string = input()
	inputStr.append(string)

Q = int(input())
for i in range(Q):
	query = input()
	occurs = countOccur(query, inputStr)
	print(occurs)