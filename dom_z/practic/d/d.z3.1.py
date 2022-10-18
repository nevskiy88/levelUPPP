#from dom_z.modul.input_split import input_split

def input_number():
    quantity = int(input())
    my_list = []
    for i in range(quantity):
        numbers = int(input())
        my_list.append(numbers)
    print(my_list)

def input_split():
    a = input().split()
    lst = []
    for i in range(len(a)):
        lst.append(a[i])
    print(lst)

