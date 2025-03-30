from logging import exception

import requests

user_word=str(input("Enter Word:")).lower()

url="https://api.dictionaryapi.dev/api/v2/entries/en/"+user_word

data=requests.get(url)
mydata=data.json()

# Allow user to insert word, print meaning found or not found

try:
    if mydata[0]["word"]==user_word:
        print("Found")
except Exception as ex:
    print("Meaning Not Found")
else:
    #q2 How many main keys are there in this API ?
    total_keys=0

    for i in range(0,len(mydata)):
        total_keys+=len(mydata[i].keys())

    print(total_keys)

    # Allow the user to insert a word, print url of audio pronunciation of that word.
    for i in range(0,len(mydata[0]["phonetics"])):
        if mydata[0]["phonetics"][i]["audio"]=="":
            continue
        else:
            print(f"Audio of word {user_word} is :",mydata[0]["phonetics"][i]["audio"])

    # Print the First Meaning of that word.

    print(mydata[0]["meanings"][0]["definitions"][0]["definition"])


    # Print the All Meaning of that word.

    for k in range(0,len(mydata[0]["meanings"])):
        if k==0:
            print(mydata[0]["meanings"][k]["partOfSpeech"])
            for i in range(0,len(mydata[0]["meanings"][k]["definitions"])):
                print("\t",mydata[0]["meanings"][0]["definitions"][i]["definition"])
        if k==1:
            print(mydata[0]["meanings"][k]["partOfSpeech"])
            for j in range(0,len(mydata[0]["meanings"][k]["definitions"])):
                print("\t",mydata[0]["meanings"][0]["definitions"][j]["definition"])

