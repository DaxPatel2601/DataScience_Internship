# tuple methods

tp=(1,2,3,2,5,6)

#count
print(tp.count(2))

#index
print(tp.index(5))

#search
user_input=int(input("Enter Value:"))

if user_input in tp:
    print("found")
else :
    print("not found")


#print all items

for i in range(0,len(tp)):
    print(tp[i])