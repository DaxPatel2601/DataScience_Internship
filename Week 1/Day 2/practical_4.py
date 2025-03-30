import requests

data=requests.get("https://api.mfapi.in/mf")
mydata=data.json()

#q1
print("q1  How many main keys are there in this API ?")
# print(mydata.keys())
# key=mydata.keys()
# print(len(key))
print("there is no keys in this api")
print("\n")

#q2
print("q2  Print total number of mutual funds")
total_numbers_mutual_funds=len(mydata)
print("Total numbers of mutual funds is :",total_numbers_mutual_funds)
print("\n")

#q3
print("q3 Print name of first mutual fund")
print("First name of mutual fund is :",mydata[0]["schemeName"])

count=0
for i in mydata:
    print(count+1," : ","\t","Scheme ID :    ",mydata[count]["schemeCode"],"\t","Scheme Name :    ",mydata[count]["schemeName"])
    count+=1