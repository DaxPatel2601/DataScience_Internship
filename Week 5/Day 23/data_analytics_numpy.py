

# Sales Data Analysis using NumPy
# Objective:
# Analyze and visualize sales data for a company’s products across four quarters using
# NumPy arrays. You will compute key metrics like total sales, average sales per product,
# and identify the best-performing product.

import pandas as pd
import numpy as np


#  Create a NumPy Array for Sales Data: Convert the sales data into a 2D NumPy array.

arr=np.array(pd.read_excel("extracted_data.xlsx").iloc[0:,1:])
print(arr)


# Compute Total Sales for Each Product: Calculate the total sales for each product
# by summing across the quarter


total_sales=[]

