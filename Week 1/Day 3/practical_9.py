import requests

#Allow user to input country name
user_country_name=str(input("Enter Your Country Name:"))

url="http://universities.hipolabs.com/search?country="+user_country_name
data=requests.get(url)
mydata=data.json()

# Print number of universities in that country
print("Total numbers of universities is : ",len(mydata))

# Print name and websites of all universities of that country using for loop.
for i in range(0,len(mydata)):
    print(i,")","University Name:",mydata[i]["name"],"\n\t","Website:",mydata[i]["web_pages"][0],"\n")

