N = int(input())
n = list(map(int,input().split()))

res = []

for i in n: 
    if i % 2 == 0 :
        res.append(i)
    elif i == 0 :
        res.append(i)

for i in res[::-1] :
    print(i, end=' ')
