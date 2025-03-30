import matplotlib.pyplot as plt

# Graph 1 : Generate pie chart from below dictionary data. Print college name in graph title.
#
Newdata = {
    "college": "Shree Raviraj",
    "seats": 890,
    "branches": 7,
    "data": [
        {"name": "CE", "allocated": 90},
        {"name": "IT", "allocated": 120},
        {"name": "MECH", "allocated": 40},
        {"name": "CSE", "allocated": 100},
        {"name": "CIVIL", "allocated": 70},
        {"name": "EC", "allocated": 15},
        {"name": "ELECTRONICS", "allocated":45}
]
}

departments=[]
allocated=[]

for i in range(0,len(Newdata["data"])):
    departments.append(Newdata["data"][i]["name"])
    allocated.append(Newdata["data"][i]["allocated"])

plt.pie(allocated,labels=departments,autopct="%.2f%%")
plt.title("Department Allocation Analysis")
plt.show()