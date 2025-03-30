# List methods

lst=["TV","monitor","AC","specker"]
print(lst)

#length
print(len(lst))

# add item at last position
new_item="keyboard"
lst.append(new_item)
print(lst)

# add item at any position
lst.insert(3,"Mouse")
print(lst)

#remove last element
lst.pop()
print(lst)

#remove element at any index
lst.remove("Mouse")
print(lst)

#changing value of list
lst[3]="AC"
print(lst)

#ascending sort
lst.sort()
print(lst)

#decending sort
lst.sort(reverse=True)
print(lst)

#print all items in list
for i in lst:
    print(i)

#print all items using range function
for i in range(0,len(lst)):
    print(lst[i])

#find any items in list
user_value=str(input("Enter value"))
if user_value in lst:
    print("item is found")
else:
    print("item is not found")

#reverse print

for i in range(len(lst)-1,-1,-1):
    print(lst[i])

# reverse without range

# for i in lst:
#