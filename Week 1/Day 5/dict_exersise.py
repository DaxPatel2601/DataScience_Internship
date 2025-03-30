# user can enter key name and print value

dic={
    "Ahemdabad":200,
    "Surat":150,
    "Rajkot":100
}

user_input=input("Enter key name:")

for i in dic.keys():
    if i==user_input:
        print(dic[i])
        break
else:
    print("not found")






