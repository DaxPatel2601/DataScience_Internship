import matplotlib.pyplot as plt
import numpy as np

branches=["CE","IT","MECH","CIVIL","EC","EE"]
seats=[100,80,40,50,20,10]

print(np.array(seats).sum())

plt.pie(seats,labels=branches,autopct="%.2f%%")

plt.show()