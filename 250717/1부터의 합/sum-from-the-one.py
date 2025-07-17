N = int(input())
add = 0

for i in range(100) :
    add += i
    if add >= N :
        print(i)
        break 