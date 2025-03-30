# create 7 column and 4 rows excel and perform search , loop , values

import xlrd
import json

# allow path
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True

loc=("excel1.xlsx")

sheet=xlrd.open_workbook(loc)
sheet=sheet.sheet_by_index(0)

main_dic={}
my_dic={}



user_input=input("X/Y?:").lower()

if user_input=="x":
    for i in range(1,sheet.ncols):
        temp_dic = {}
        for j in range(1,sheet.nrows):
            x=sheet.cell_value(j,i)
            temp_dic[sheet.cell_value(j,0)]=x
            my_dic[f"{sheet.cell_value(0,i)}"]=temp_dic

elif user_input=="y":
    for i in range(1,sheet.nrows):
        temp_dic = {}
        for j in range(1,sheet.ncols):
          x=sheet.cell_value(i,j)
          temp_dic[sheet.cell_value(0,j)]=x
          my_dic[int(sheet.cell_value(i,0))]=temp_dic
    main_dic[sheet.cell_value(0,0)]=my_dic

else:
    print("Invalid input!!")

print(main_dic)