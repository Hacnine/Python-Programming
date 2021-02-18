from openpyxl import Workbook
import xlsxwriter
# for more details visit http://zetcode.com/python/openpyxl/
import openpyxl

book = openpyxl.load_workbook('transactions.xlsx')

sheet = book.active

a1 = sheet['A1']
a2 = sheet['A2']
a3 = sheet.cell(row=4, column=4, value=999)

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

book.save('transactions.xlsx')
print(a3.value)