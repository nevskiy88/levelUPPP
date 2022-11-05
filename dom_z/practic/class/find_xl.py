import openpyxl
file = openpyxl.reader.excel.load_workbook(filename = 'teams.xlsx')
sheet = file['список1']


#sheet = file.act
# print(sheet['A3'].value)
proba_number = input("введите название пробы: ")
for i in range(2, 312):
        if proba_number in sheet['A' +str(i)].value:
            print(f" Название: {sheet['A'+str(i)].value}, Интервал: {sheet['B'+str(i)].value} Тара:{sheet['C'+str(i)].value} Примечание: {sheet['D'+str(i)].value} Где: {sheet['E'+str(i)].value}" )
