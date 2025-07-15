a, b = map(int, input().split())

arr = [a, b]

for i in range(2, 10) :
    add = arr[i-2] + arr[i-1]
    if add >= 10 :
        add -= 10
    arr.append(add)

for i in arr :
    print(i, end=' ')