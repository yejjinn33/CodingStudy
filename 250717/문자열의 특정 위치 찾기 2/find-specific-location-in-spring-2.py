a = input()
string = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for i in string :
    if i[2] == a :
        print(i)
        cnt += 1
    elif i[3] == a :
        print(i)
        cnt += 1

print(cnt)
    