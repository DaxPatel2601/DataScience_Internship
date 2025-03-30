import requests

data=requests.get("https://isro.vercel.app/api/spacecrafts")
mydata=data.json()

my_lst=[]

for i in range(0,len(mydata["spacecrafts"])):
    my_lst.append(mydata["spacecrafts"][i]["name"])

File=open("ISRO.txt",'w')

# write list into file

for i in my_lst:
    File.write(f"{i}\n")
File.close()




