import openpyxl as pyxl
from converter import convertToDuration




# Loading Excel workbook to work on
wb = pyxl.load_workbook(filename = '2023_usage_dataset.xlsx')
ws = wb['2023_Usage']


# Cell range to transform
cell_range = ws['B2':'BT214']


# Transforming each cell values based on specified range
for rows in cell_range:
    for each in rows:
        each.value = convertToDuration(each.value)



wb.save(filename = '2023_usage_dataset.xlsx')