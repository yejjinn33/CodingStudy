N, M = map(int, input().split())

# Please write your code here.
print(N)
while True:
    if N//M <= 0 :
        break
    print(N // M)
    N = N // M
    