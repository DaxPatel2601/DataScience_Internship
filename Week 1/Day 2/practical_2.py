# data fetching from API

mydata= {"category":[{"A":"FIRST","package":{"data":"2lacs"}},
{"B":"Second","data":{"new":[100]}},{"C":"Third","Tests":[45,75,25]}]};

#q1
print("Q1 Print 2lacs")
print(mydata["category"][0]["package"]["data"])
print("\n")

#q2
print("q2 Print 25")
print(mydata["category"][2]["Tests"][2])
print("\n")

#q3
print("q3 Print 100")
print(mydata["category"][1]["data"]["new"][0])