import numpy as np
import requests

url=requests.get("http://universities.hipolabs.com/search?country=india")
my_data=url.json()

# fetch the list of universities

university_arr=np.array([])

for i in range(0,len(my_data)):
    print(my_data[i]["name"])


# determin the numbers of universities

print(len(my_data))


# generate unique random numbers as indices

unique_arr=np.random.randint(0,5000,len(my_data))
print(unique_arr)

# stored universities into an array

for i in range(0,len(my_data)):
    university_arr=np.append(university_arr,my_data[i]["name"])

print(university_arr)

# create Numpy structure array with generated indices and universities names

