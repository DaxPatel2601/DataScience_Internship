import requests

data=requests.get("http://universities.hipolabs.com/search?country=india")
mydata=data.json()


# collect all universities names and stored into list

universities=[]

for i in range(0,len(mydata)):
    universities.append(mydata[i]["name"])

print(universities)

use_input=input("Enter New University :")

if use_input in universities:
    print("This University is already exist")
else:
    universities.append(use_input)
    print(f"{use_input} is insert successfully")

print(universities)


