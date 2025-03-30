import matplotlib.pyplot as plt

# Advance PIE

car_names=["Hyundai","Maruti","TATA","Ford"]
car_unites=[12000,24000,20000,1500]
colors=["RED","GREEN","BLUE","YELLOW"]

plt.pie(car_unites,labels=car_names,autopct="%.2F%%",explode=(0.1,0,0,0),colors=colors,shadow=(0.2,0,0,0))
plt.legend()
plt.title("Car Sales Analysis")
plt.figimage()
plt.show()