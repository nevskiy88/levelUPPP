def eee(lst,min_a, max_a):
    total = []

    for i in range(len(lst)-1):
        if i < min_a and i > max_a:
            continue
        else:
            total.append(lst[i])

    return total

aa = input().split()
xx = []
for i in range(len(aa)):
    xx.append(aa[i])
min_a = int(input())
max_a = int(input())

cc = eee(aa,min_a,max_a)
print(cc)