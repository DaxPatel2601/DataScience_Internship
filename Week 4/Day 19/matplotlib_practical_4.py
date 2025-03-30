from cProfile import label

import xlrd
import matplotlib.pyplot as plt

# Graph 4 : IMPORTANT
#
# Download following customer data
# https://docs.google.com/spreadsheets/d/1x9hgRj1jqV5H9BRXAY397ljhpBtrpKWDLYyrwwentIU/edit?usp=sharing
#
# Print following pie charts from above data
# Pie Chart 1 : Percentage of male and female from gender column.


sheet=xlrd.open_workbook("customer.xlsx").sheet_by_index(0)
count_male=0
count_female=0
review_avegrage=0
review_poor=0
review_good=0
school=0
pg=0
ug=0



for i in range(1,sheet.nrows):
    if sheet.cell_value(i,1)=="Male":
        count_male+=1
    if sheet.cell_value(i,1)=="Female":
        count_female+=1
    if sheet.cell_value(i,2)=="Average":
        review_avegrage+=1
    if sheet.cell_value(i,2)=="Poor":
        review_poor+=1
    if sheet.cell_value(i,2)=="Good":
        review_good+=1
    if sheet.cell_value(i,3)=="School":
        school+=1
    if sheet.cell_value(i,3)=="PG":
        pg+=1
    if sheet.cell_value(i,3)=="UG":
        ug+=1


plt.pie([count_male,count_female],labels=["Male","Female"],autopct="%.2f%%",)
plt.title("Percentage of male and female from gender column.")
plt.show()


# Pie Chart 2 : Percentage of Average, Poor and Good from review column.

plt.pie([review_avegrage,review_good,review_poor],labels=["Average","Good","Poor"],autopct="%.2f%%")
plt.title("Percentage of Average, Poor and Good from review column.")
plt.show()

# Pie Chart 3 : Percentage of School, UG and PG from education column.

plt.pie([school,pg,ug],labels=["School","PG","UG"],autopct="%.2f%%")
plt.title("Percentage of Average, Poor and Good from review column.")
plt.show()


# percentage of male and females who`s age is between 18 to 50

male1=0
female1=0

for i in range(1,sheet.nrows):
    if (sheet.cell_value(i,0)>=18) and (sheet.cell_value(i,0)<=50):
        if sheet.cell_value(i,1)=="Male":
            male1+=1
        if sheet.cell_value(i,1)=="Female":
            female1+=1


plt.pie([male1,female1],labels=["Male","Female"],autopct="%.2f%%")
plt.title("percentage of male and females who`s age is between 18 to 50")
plt.show()
print(male1)
print(female1)