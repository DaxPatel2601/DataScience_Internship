# Graph 5 : matplotlib + Json / Dictionary.
#
# Generate 3 bar graphs in a single row for comparison of all players ( matches vs score ).
# chart from below dictionary data. Print college name in graph title.
#
import matplotlib.pyplot as plt

mydata={
  "Format": "ODI",
  "MATCHES": 5,
  "data": [
    {
      "Match": "Match 1",
      "ROHIT": 75,
      "KOHLI": 21,
      "DHAVAN": 40
    },
    {
      "Match": "Match 2",
      "ROHIT": 15,
      "KOHLI": 111,
      "DHAVAN": 10
    },
    {
      "Match": "Match 3",
      "ROHIT": 25,
      "KOHLI": 4,
      "DHAVAN": 70
    },
    {
      "Match": "Match 4",
      "ROHIT": 45,
      "KOHLI": 15,
      "DHAVAN": 80
    },
    {
      "Match": "Match 5",
      "ROHIT": 5,
      "KOHLI": 78,
      "DHAVAN":20
}
]
}

matches=[]
rohit_score=[]
kohli_score=[]
dhavan_score=[]

for i in range(0,len(mydata["data"])):
    rohit_score.append(mydata["data"][i]["ROHIT"])
    kohli_score.append(mydata["data"][i]["KOHLI"])
    dhavan_score.append(mydata["data"][i]["DHAVAN"])
    matches.append(mydata["data"][i]["Match"])



fig,axs = plt.subplots(1,3,figsize=(8,5))
axs[0].bar(matches,rohit_score)
axs[1].bar(matches,kohli_score)
axs[2].bar(matches,dhavan_score)
plt.tight_layout()
plt.show()


