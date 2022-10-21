my_list= {}
a = [1, 2, 3, 4, 5]
b = [111, 222, 333, 444, 555]
s = zip(a, b)
d = list(s)
for i in d:
    my_list[i[0]] = i[1]
print(my_list)
