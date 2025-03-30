from matplotlib import pyplot as plt

Players=["Rohit","Kohli","Dhoni"]
Runs=[100,50,65]

plt.xlabel("Players")
plt.ylabel("Runs")
plt.title("Player Score Analysis")

plt.bar(Players,Runs)
plt.show()

