import requests

data=requests.get("https://api.postalpincode.in/pincode/380009")
mydata=data.json()

#q1
print("q1   How many main keys are there in this API ?")
print("there is no keys in this dictionary")
print("\n")

#q2
print("q2 Print Ashram Road")
print(mydata[0]["PostOffice"][0]["Name"])
print("\n")

#q3
print("Print total count of areas under this Pin Code")
print("Total areas in this pin code is :",len(mydata[0]["PostOffice"]))

count=0
for i in mydata[0]["PostOffice"]:
    print(count+1,"\t","Area Name : ",mydata[0]["PostOffice"][count]["Name"])
    count+=1



