import numpy as np

#1. Data Loading and Exploration

# Load the dataset into a NumPy array using np.genfromtxt().
data=np.genfromtxt("Sales_Data.csv",dtype=None,delimiter=",",names=True)


# Explore the dataset:

print(data)

transaction=data["TransactionID"]
product=data["Product"]
quantity=data["Quantity"]
price=data["Price"]
date=data["Date"]

# Find the total number of transactions.
print(f"Total number of transactions are {len(transaction)}")

# Identify the unique products sold.
print(f"Unique Products are {np.unique(product)}")

# Check for missing values and handle them (e.g., replace with 0 or remove rows).

# data[np.where(np.isnan(price))]=0
data[np.where(np.isnan(transaction))]=0


# 2. Basic Calculations
# Calculate the total revenue for each transaction (Revenue = Quantity * Price).

total_revenue=0

for i in range(0,len(transaction)):
    total_revenue+=quantity[i]*price[i]
    print(f"Total Revenue of Transaction ID {transaction[i]} {product[i]}: {quantity[i]*price[i]}")

# Compute the total revenue for the entire dataset.

print("Total Revenue is ",total_revenue)

# Find the average price of products sold.
print("average price of products sold is",np.mean(price))

# Calculate the total quantity sold for each product.

unique_products=np.unique(product)

for i in unique_products:
    quantity_all=np.sum(quantity[product==i])
    print(f"Total Quantity Sold of {i} is {quantity_all}")


# 3. Advanced Calculations

# Find the product with the highest total revenue.

revenue=np.array([])
revenue_product=np.array([])

for i in unique_products:
    total_revenue_each=np.sum(quantity[product==i]*price[product==i])
    print(f"Total Quantity Sold of {i} is {total_revenue_each}")
    revenue=np.append(revenue,total_revenue)
    revenue_product=np.append(revenue_product,i)

print(revenue)
# print(np.max(revenue))



# Compute the total revenue for each day (group by Date).


# Find the day with the highest total revenue.






