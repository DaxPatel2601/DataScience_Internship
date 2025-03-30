
# User can add new key value pair , if key is already exists than return , this process is continue until user can stop this process

cities={
    "Ahemdabad":150,
    "Surat":100,
    "Rajkot":50,
    "Vadodara":200
}


is_stop=False
count=1

while True:
    if is_stop==False:
        user_new_key_name=str(input(f"Enter {count} Key Name:"))
        if user_new_key_name in cities:
            print("This key is already exist")
            break
        user_new_value=int(input(f"Enter {count} key Value:"))
        cities[user_new_key_name]=user_new_value
        print("New key and value is added successfully")
        print(cities)
    else:
        print("This Process is Stopped!!")
        break

    Stop=input("Do you Wanna Stop this process(Y/N)")
    if Stop=="Y":
     is_stop=True
    elif Stop=="N":
     is_stop=False
    else:
        print("Invalid Input!!")

    count+=1