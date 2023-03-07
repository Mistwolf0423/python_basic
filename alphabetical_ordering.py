s = input()
a = []
b = []
c = []
d = []

for char in s:
    if char.isnumeric():
        if int(char)%2 == 0:
            d.append(char)
        else:
            c.append(char)
    else:
        if char.isupper():
            a.append(char)
        else:
            b.append(char)

print(''.join(sorted(b))+''.join(sorted(a))+''.join(sorted(c))+''.join(sorted(d)))