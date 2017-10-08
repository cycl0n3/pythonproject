import openpyxl
import bleach

wb = openpyxl.load_workbook('data/example.xlsx')

print(type(wb))
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet3')
print(type(sheet))
print(sheet.title)
anotherSheet = wb.get_active_sheet()
print(anotherSheet)

print('-'*20)

sheet = wb.get_sheet_by_name('Sheet1')
print(sheet['A1'].value)
c = sheet['B1']
print(c.value)
print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)
print('Cell ' + c.coordinate + ' is ' + c.value)
print(sheet['C1'].value)
