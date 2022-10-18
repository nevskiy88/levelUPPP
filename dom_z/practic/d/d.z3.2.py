def calculator_split():
    a = input().split()
    lst = []
    for i in range(len(a)):
        lst.append(a[i])
    return lst


def calculator(lst):
    if lst[1] == '+':
        print(int(lst[0]) + int(lst[2]))
    elif lst[1] == '-':
        print(int(lst[0]) - int(lst[2]))
    elif lst[1] == '*':
        print(int(lst[0]) * int(lst[2]))
    elif lst[1] == '/':
        if lst[2] == "0":
            print('на ноль делить нельзя')
        else:
            print(int(lst[0]) / int(lst[2]))

a = calculator_split()

calculator(a)