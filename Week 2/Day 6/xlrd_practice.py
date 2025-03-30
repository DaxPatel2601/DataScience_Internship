import xlrd

# cricket analysis

# allow path
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True

loc=("excel1.xlsx")
sheet=xlrd.open_workbook(loc)

sheet=sheet.sheet_by_index(0)

print(sheet)

# printing first element
print(sheet.cell_value(0,0))

# print total numbers of rows and columns

print("Total rows is ",sheet.nrows)
print("Total column is ",sheet.ncols)


# print total runs
total_rohit=0
total_kohli=0
total_hardik=0

for i in range(1,sheet.nrows):
    total_rohit+=sheet.cell_value(i, 1)

for i in range(1,sheet.nrows):
    total_kohli+=sheet.cell_value(i, 2)

for i in range(1,sheet.nrows):
    total_hardik+=sheet.cell_value(i, 3)

print("Total Runs Of Rohit is :",int(total_rohit))
print("Total Runs Of Kohli is :",int(total_kohli))
print("Total Runs Of Hardik is :",int(total_hardik))


# print name of all players
for i in range(1,sheet.ncols):
    print(sheet.cell_value(0,i))

# allow user to enter of players name and print found or not

user_search=input("Enter Player Name:")
for i in range(1,sheet.ncols):
    if user_search==sheet.cell_value(0,i):
        print("player found")
        break
else:
    print("not found")


user_search1=input("Enter Player Name:")

for i in range(1,sheet.ncols):
    if user_search1==sheet.cell_value(0,i):
        print(sheet.cell_value(sheet.nrows-1,i))
        break
else:
    print("not found")




