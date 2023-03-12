ls = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    ls.append([name, score])
point = [x[1] for x in ls]
ls_2 = sorted(set(point))
final = sorted([y[0] for y in ls if y[1] == ls_2[1]])
[print(k) for k in final]
