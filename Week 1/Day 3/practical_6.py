import requests

data=requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
mydata=data.json()

#q1 How many main keys are there in the API ? count ?

main_key=mydata.keys()
print(len(main_key))

#q2  Print names of all main keys.

print(main_key)

# q3  Print 2021

print(mydata["data"][1]["Year"])

#q4 How many years of data are available ?

print(len(mydata["data"]))

'''q5 Print all Data using for loop as below format 
	1 Year 2022 USA POPULATION 331097593
	2 Year 2021 USA POPULATION '''

count=0
for i in mydata["data"]:
    print(count+1,"Year:",mydata["data"][count]["Year"],"\t","Nation:",mydata["data"][count]["Nation"],"\t","Population:",mydata["data"][count]["Population"])
    count+=1
