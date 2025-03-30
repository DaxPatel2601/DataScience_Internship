import numpy as np
import requests

url=requests.get("http://universities.hipolabs.com/search?country=india")
my_data=url.json()


# Fetch the university data from the API.

university_arr=np.array([])

for i in range(0,len(my_data)):
    print(my_data[i]["name"])

# Generate unique random numbers as Unicode indices.

unique_arr=np.random.randint(0,5000,len(my_data))
print(unique_arr)

#  Store university names in a NumPy array.
university_arr=np.array([])

for i in range(0,len(my_data)):
    university_arr=np.append(university_arr,my_data[i]["name"])

print(university_arr)

# Save the NumPy array to an Excel file using numpy.savetxt() in CSV format.
# file must be csv formate

np.savetxt("data.csv",university_arr,fmt="%s")


