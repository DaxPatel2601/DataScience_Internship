import xlrd

sheet=xlrd.open_workbook("storedata.xlsx")
sheet=sheet.sheet_by_index(0)

# PRINT TOTAL NUMBER OF ROWS
print("Total Number of Rows are :",sheet.nrows)

# PRINT TOTAL NUMBER OF COLUMNS
print("Total Number Of Columns are :",sheet.ncols)

# PRINT 61
print(sheet.cell_value(sheet.nrows-1,sheet.ncols-1))

# PRINT NAMES OF ALL MONTHS
for i in range(1,sheet.ncols):
     print(sheet.cell_value(0,i) , end=" ")
print()

# PRINT NAMES OF ALL PRODUCTS
for i in range(1,sheet.nrows):
    print(sheet.cell_value(i,0),end=" ")
print()

# PRINT TOTAL NUMBER OF PRODUCTS SOLD IN MARCH MONTH

Total_sale_march=0

for i in range(1,sheet.ncols):
    if sheet.cell_value(0,i)=="MARCH":
        for j in range(1,sheet.nrows):
            Total_sale_march+=sheet.cell_value(j,i)

print(Total_sale_march)

# WHICH PRODUCT SOLD HIGHEST IN MARCH MONTH.  ( ANS MOBILES )

max_sale_march=0

for i in range(1,sheet.ncols):
    if sheet.cell_value(0,i)=="MARCH":
        for j in range(1,sheet.nrows):
            if max_sale_march<sheet.cell_value(j,i):
                max_sale_march=sheet.cell_value(j,i)

        for k in range(1,sheet.nrows):
            if sheet.cell_value(k,i)==max_sale_march:
                print("Max Product Sold In March is :",sheet.cell_value(k,0))

# ALLOW USER TO INSERT NAME OF THE MONTH PRINT NAME OF HIGHEST AND LOWEST NUMBER OF PRODUCTS SOLD IN THAT MONTH

user_month_name=input("Enter Month Name : ").upper()

highest_sold=0

for i in range(1,sheet.ncols):
    if user_month_name==sheet.cell_value(0,i):
        minimum_sold=sheet.cell_value(1,i)

        for j in range(1,sheet.nrows):
            if highest_sold < sheet.cell_value(j, i):
                highest_sold = sheet.cell_value(j, i)

            if minimum_sold>sheet.cell_value(j,i):
                minimum_sold=sheet.cell_value(j,i)

        for k in range(1,sheet.nrows):
            if sheet.cell_value(k,i)==highest_sold:
                print(f"Max Sold Product In {sheet.cell_value(0,i)} is:",sheet.cell_value(k,0))
            if sheet.cell_value(k,i)==minimum_sold:
                print(f"Max Sold Product In {sheet.cell_value(0,i)} is:",sheet.cell_value(k,0))
        break
else:
    print("Month Name is not found!!")


# IN WHICH MONTH REFRIGERATOR SOLD HIGHEST.

max_sale_of_refrigerator=0

for i in range(1,sheet.nrows):
    if sheet.cell_value(i,0)=="REFRIGERATOR":
        for j in range(1,sheet.ncols):
            if max_sale_of_refrigerator<sheet.cell_value(i,j):
                max_sale_of_refrigerator=sheet.cell_value(i,j)

        for k in range(1,sheet.ncols):
            if sheet.cell_value(i,k)==max_sale_of_refrigerator:
                print(sheet.cell_value(0,k))

# ALLOW USER TO INSERT NAME OF ELECTRONIC DEVICE. PRINT IN WHICH MONTH IT SOLD HIGHEST.

for i in range(1,sheet.nrows):
    print(sheet.cell_value(i,0),end=" | ")
print()

user_electric_device=input("Enter Electric Device Name:").upper()

for i in range(1,sheet.nrows):
    if sheet.cell_value(i,0)==user_electric_device:
        for j in range(1,sheet.ncols):
            if max_sale_of_refrigerator<sheet.cell_value(i,j):
                max_sale_of_refrigerator=sheet.cell_value(i,j)

        for k in range(1,sheet.ncols):
            if sheet.cell_value(i,k)==max_sale_of_refrigerator:
                print(f"Highest {sheet.cell_value(i,0)} Sold In",sheet.cell_value(0,k))
        break
else:
    print("Electric Device Not Found")