a = input()

a1 = a.replace(a[1], "a", 1)
a2 = a1.replace(a[-2], "a", 1)

print(a2)