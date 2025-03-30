import requests

data=requests.get("https://isro.vercel.app/api/spacecrafts")
mydata=data.json()

#  Allow user to enter ID. Print that spacecraft’s name


user_id=str(input("Enter Id for Search spacecrafts:"))
for i in range(0,len(mydata["spacecrafts"])):
    if user_id==str(mydata["spacecrafts"][i]["id"]):
        print("Name:",mydata["spacecrafts"][i]["name"])
        break
else:
    print("This Id is not found")

#Allow user to insert name of space craft. Print that spacecraft is launched by isro or not.


user_spacecarft=str(input("Enter Spacecraft Name:"))

for i in range(0,len(mydata["spacecrafts"])):
    if user_spacecarft==str(mydata["spacecrafts"][i]["name"]):
        print("This spacecraft is launched by ISRO")
        break
else:
    print("This spacecraft is not launched by ISRO ")
