import matplotlib.pyplot as plt
import numpy as np

# multiple lines

matches=[1,2,3,4,5]
rohit=[100,20,30,45,88]
kohli=[11,25,100,85,48]
dhoni=[90,0,10,60,70]
barwidth=0.15

plt.bar(np.arange(len(matches)),rohit,width=barwidth,label="ROHIT")
plt.bar(np.arange(len(matches))+0.15,kohli,width=barwidth,label="KOHLI")
plt.bar(np.arange(len(matches))+0.30,dhoni,width=barwidth,label="DHONI")

plt.legend()
plt.show()