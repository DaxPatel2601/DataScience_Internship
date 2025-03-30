# working with API

mydata= {
"maharashtra":{"mumbai":{"city":"metro city","metro":"yes"}, "population":"20 cr"},
"gujarat": ["AHMEDABAD","SURAT","RAJKOT"],
"rajasthan":["AJMER","JAISALMER",{"capital":"jaipur"},["MEWAD","RJ","INR"]]
}

#q1
print("Print metro city")
print(mydata["maharashtra"]["mumbai"]["city"])
print("\n")

#q2
print("Print jaipur")
print(mydata["rajasthan"][2]["capital"])
print("\n")

#q3
print("Print RJ")
print(mydata["rajasthan"][3][1])