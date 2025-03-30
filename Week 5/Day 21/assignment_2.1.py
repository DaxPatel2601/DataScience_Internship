# AMAZON CATEGORIES DATASET
#
#
import xlrd

# 1) Load amazon categories dataset.
sheet=xlrd.open_workbook("New Microsoft Excel Worksheet.xlsx").sheet_by_index(0)

# 2) Print total number of rows.
print(sheet.nrows)

# 3) Print total number of columns.
print(sheet.ncols)

# 4) Print names of all columns.

for i in range(0,sheet.ncols):
    print(sheet.cell_value(0,i))




