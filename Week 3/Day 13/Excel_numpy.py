import numpy as np
from numpy.ma.core import maximum

data=np.genfromtxt("numpy_analysis_data.csv",dtype=None,delimiter=",",names=True)

print(data)

id=data["ID"]
age=data["Age"]
salary=data["Salary"]
experience=data["Experience"]
department=data["Department"]

print(id)
print(age)
print(salary)
print(experience)
print(department)


# find unique departments

unique_departments=np.unique(department)
print(unique_departments)

# find average salary

print(np.mean(salary))

# find minimum and maximum salary

print(np.max(salary))
print(np.min(salary))

# stored unique departments into dectionary

my_dic={}

for i in unique_departments:
    salary_unique=np.sum(salary[department==i])
    my_dic[i]=salary_unique

print(my_dic)

for k,v in my_dic.items():
    print(k , v)

# salary between 50000 to 80000

print(salary[np.where((salary<=80000) & (salary>=50000))])

# print percentage of every department total salary with sum of all

total_salay=np.sum(salary)
print()

for i in unique_departments:
    percentage=(my_dic[i]/total_salay)*100
    print(f"percentage of {i} is {percentage} %")

