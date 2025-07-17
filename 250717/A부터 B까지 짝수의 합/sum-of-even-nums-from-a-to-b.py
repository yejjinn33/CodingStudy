A, B = map(int, input().split())
res = 0

for i  in range(A, B+1) :
    if i % 2 == 0 :
        res += i
    else :
        continue
print(res)