import requests

data=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
mydata=data.json()

#q1
print("Q1  How many main keys are there in this API ?")
key=mydata.keys()
print("Keys are:",key)
print("\n")

#q2
print("Q2   Print total count ( number ) of main keys.")
print("Total number of keys are :",len(key))
print("\n")

# this is second method
keys_count=0
for i in key:
    keys_count+=1
print(keys_count)

#q3
print("Q3 Print Bitcoin prices in USD")
print("Bitcoin prince in USD is:",mydata["bpi"]["USD"]["rate"])