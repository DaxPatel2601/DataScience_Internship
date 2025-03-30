import xlrd

loc=("excel1.xlsx")
sheet=xlrd.open_workbook(loc)
sheet=sheet.sheet_by_index(0)

user_player=input("Enter Player Name :")
max=0
for i in range(1,sheet.ncols):
   if user_player==sheet.cell_value(0,i):
       for j in range(1,sheet.nrows):
           if max<=sheet.cell_value(j,i):
               max=sheet.cell_value(j,i)
       break
else:
    print("not Found")
print(max)

print(max/sheet.nrows)
