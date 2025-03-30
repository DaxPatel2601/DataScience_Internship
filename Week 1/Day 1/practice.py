# fetching data from API
# use json formatter website for better understanding of APIs
# javascript object notation (json)
# offline --> dictionary
# online --> APIs

import requests

# this sentence is used for request to the host and receive response from the server
data=requests.get("https://isro.vercel.app/api/launchers")
print(type(data))

# this step is convert response to dictionary variable
my_data=data.json()

print(type(my_data))

#printing all keys
print(my_data.keys())

#printing all values
print(my_data.values())
print(my_data["launchers"][26])


