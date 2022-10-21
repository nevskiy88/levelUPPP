my_dict ={
1:  ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
2:	["D", "G"],
4:	["F", "H", "V", "W", "Y"],
3:	["B", "C", "M", "P"],
5:	["K"],
8:	["J", "X"],
10: ["Q", "Z"]
}

slovo = input("введите слово   ").upper()
my_list = []
for i in slovo:
    my_list.append(i)
total = 0
for j in my_list:
    for k,v in my_dict.items():
        if j in v:
            total +=k
print(total)