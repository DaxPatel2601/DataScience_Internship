import pandas as pb
import matplotlib.pyplot as plt

data_pb=pb.read_csv("20_feb.csv")

# Create a DataFrame
# Create a Pandas DataFrame with columns: Name, Age, City, and Salary for 5 employees.

# print(data_pb)

# Basic Information & Summary
# Display the first 3 rows of the DataFrame.
# print(data_pb.head(3))
# Show the column names, data types, and summary statistics.
# print(data_pb.info())


# Indexing & Selecting Data
# Retrieve all employees who live in New York.
# print(data_pb[data_pb["City"]=="New York"])

# Extract the Name and Salary columns only.
# print(data_pb[["Name","Salary"]])

# Filtering Data
# Find employees who earn more than $5000.
# print(data_pb[data_pb["Salary"]>7000])

# Find employees whose name starts with 'A'.
# x=data_pb[data_pb["Name"].str.startswith("A")]
# print(x)

# Handling Missing Data
# Introduce some NaN values in the Salary column and replace them with the column’s mean.
# is_nan=data_pb.fillna(data_pb["Salary"].mean())
# print(is_nan)

# Drop any rows where Age is missing.
# data_pb["Age"].dropna()

# Sorting Data
# Sort the DataFrame by Salary in descending order.
# print(data_pb["Salary"].sort_values(ascending=False))

# GroupBy & Aggregations
# Group employees by City and find the average salary in each city.
# print(data_pb.groupby("City")["Salary"].mean())

# Apply Functions
# Create a new column Salary_After_Tax, where each employee's salary is reduced by 10%

# percentage=10
# data_pb["Salary_After_Tax"]=data_pb["Salary"]*(1-(percentage/100))
# print(data_pb)

# to_csv for updating excel file
# data_pb.to_csv("20f.csv",index=True)

# Merging & Joining Data
# Create another DataFrame containing Department information and merge it with the existing employee DataFrame.

# data_pb["NEW"]=data_pb[["Name","Department"]].agg(' '.join,axis=1)
# print(data_pb)
age_unique=data_pb["Age"].unique()

data_pb.plot(kind = 'scatter', x = 'Age', y = 'Salary')
plt.xticks(age_unique)
plt.show()