a = input()
aa = len(a)

a = a[:1] + "a" + a[2:]
a = a[:aa-2] + "a" + a[aa-1:]

print(a)