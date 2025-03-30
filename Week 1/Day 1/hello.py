print("hello")

name="dax"
age=20
height=5.11
is_student=True

print(name," ", type(name))
print(age," ", type(age))
print(height," ", type(height))
print(is_student," ", type(is_student))

# fetching data form API using requests package

import requests

data=requests.get("https://isro.vercel.app/api/spacecrafts")
print(type(data))

mydata=data.json()
print(type(mydata))


print(mydata["spacecrafts"][0]["name"])


lst=[1,2,8,54,1,8,1,5,2,4]
print(lst.count(1))
