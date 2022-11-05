import openpyxl
file = openpyxl.reader.excel.load_workbook(filename = 'teams.xlsx')
# print(file.sheetnames)
file.active = 0

sheet = file.active
# print(sheet['A3'].value)
proba_number = input("введите название пробы: ").upper()
for i in range(2, 312):
    for proba_number in sheet:
        if proba_number == i:
            print(f" Название: {sheet['A'+str(i)].value}, Интервал: {sheet['B'+str(i)].value} Тара:{sheet['C'+str(i)].value} Примечание: {sheet['D'+str(i)].value} Где: {sheet['E'+str(i)].value}" )
