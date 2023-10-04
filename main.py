import openpyxl as pyxl
from converter import convertToDuration





wb = pyxl.load_workbook(filename = 'test_pyxl.xlsx')

ws = wb.active
ws.title = 'Phone_Usage'

cell_range = ws['A1':'C3']



for rows in cell_range:
    for each in rows:
        each.value = convertToDuration(each.value)
        


wb.save(filename = 'test_pyxl.xlsx')    