import requests

url="https://api.rootnet.in/covid19-in/stats/latest"

data=requests.get(url)
mydata=data.json()

print(len(mydata.keys()))

print(len(mydata["data"]["regional"]))


for i in range(0,len(mydata["data"]["regional"])):
    print("State Name :",mydata["data"]["regional"][i]["loc"],"\t","No of indian cases:",mydata["data"]["regional"][i]["confirmedCasesIndian"],"\t","No of Foreign cases:",mydata["data"]["regional"][i]["confirmedCasesForeign"])

count=0

for i in range(0,len(mydata["data"]["regional"])):
    if mydata["data"]["regional"][i]["confirmedCasesIndian"] > 1000000:
        count+=1

print(count)


min_cases=int(input("Enter minimum cases:"))
max_cases=int(input("Enter Maximum cases:"))


for i in range(0,len(mydata["data"]["regional"])):
    if mydata["data"]["regional"][i]["confirmedCasesIndian"]>min_cases and mydata["data"]["regional"][i]["confirmedCasesIndian"]<max_cases:
        print(mydata["data"]["regional"][i]["loc"])


#new question : print highest cases in digits
Maximum_case=mydata["data"]["regional"][0]["confirmedCasesIndian"]

for i in range(0,len(mydata["data"]["regional"])):

    if Maximum_case<mydata["data"]["regional"][i]["confirmedCasesIndian"]:
        Maximum_case=mydata["data"]["regional"][i]["confirmedCasesIndian"]

print(Maximum_case)

for i in range(0,len(mydata["data"]["regional"])):
    if Maximum_case==mydata["data"]["regional"][i]["confirmedCasesIndian"]:
        print(mydata["data"]["regional"][i]["loc"])


minimum_death_cases=mydata["data"]["regional"][0]["deaths"]
index=0
for i in range(0,len(mydata["data"]["regional"])):
    if minimum_death_cases>mydata["data"]["regional"][i]["deaths"]:
        minimum_death_cases=mydata["data"]["regional"][i]["deaths"]
        index=i
print(mydata["data"]["regional"][index]["loc"],":",minimum_death_cases)


#allow user to insert state print death rate of that state in percentage

user_state_name=input("Enter state name:")
percentage=0
for i in range(0,len(mydata["data"]["regional"])):
    if user_state_name==mydata["data"]["regional"][i]["loc"]:
        percentage=(mydata["data"]["regional"][i]["deaths"])*100/(mydata["data"]["regional"][i]["confirmedCasesIndian"])
        print(f"{user_state_name} : {percentage} %")
        break
else:
    print("State is not Found")

