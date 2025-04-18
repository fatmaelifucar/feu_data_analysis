# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:15:44 2025

@author: Elif
"""

#COLUMN DESCRIPTIONS
#TransactionID: A unique identifier for each transaction. 
#CustomerID: Customer identifier, helpful for analyzing customer behavior.
#ProductID: Product identifier; repeated when the same product is purchased 
#           multiple times.
#TransactionDate: Identifies the date.
#Quantity: Number of units sold. 
#TotalValue: Quantity * Price
#Price: Unit price of the product (in local currency).

#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Dataset
file_path = "C:\\Users\\Elif\\Downloads\\transactions_data.csv"
data2024 = pd.read_csv(file_path)

#Cleaning the dataset: We only want to analyze the data belong to 2024.
#So filter out the ones belong to 2023.
data2024['TransactionDate'] = pd.to_datetime(data2024['TransactionDate'])
def filter_dates(dataframe): 
    data2024['Year'] = data2024['TransactionDate'].dt.year 
    filtered_data2024 = data2024[data2024['Year'] == 2024] 
    return filtered_data2024.drop(columns=['Year'])

data2024 = filter_dates(data2024) 
print(data2024)

#The dataset only has date column, but adding a month and hour column 
#will make the analysis part easier.
data2024.dropna(inplace = True)
data2024['TransactionDate'] = pd.to_datetime(data2024['TransactionDate'])
data2024['Month'] = data2024['TransactionDate'].dt.month
data2024['TransactionDate'] = pd.to_datetime(data2024['TransactionDate'])
data2024['Hour'] = data2024['TransactionDate'].dt.hour
print(data2024)

#Calculating some properties on the dataset

#Calculate total sales by month
sales_by_month = data2024.Month.value_counts()
print(sales_by_month)

#We find out November was the month with the fewest sales, so to 
#increase monthly sales, we will apply a discount to the products.
def apply_discount(price, discount): 
    return price * (1 - discount)
def update_prices(dataframe): 
    discount = 0.10 
    for index, row in data2024.iterrows(): 
        if row['Month'] == 11: 
            data2024.at[index, 'Price'] = apply_discount(row['Price'], discount) 
    return data2024

update_prices(data2024)
print(data2024)

#Calculate total sales by hour
sales_by_hour = data2024.Hour.value_counts()
print(sales_by_hour)

#The total sales by product
sales_by_product = data2024.ProductID.value_counts()
print(sales_by_product)

#Show which customers shopped more in 2024
sales_by_customer = data2024.CustomerID.value_counts()
print(sales_by_customer)

#Calculate each customers' purchase frequency and sort the results in descending order
purchase_frequency_by_customer = data2024.groupby(['CustomerID']).Month.agg([len, min, max])
sorted_pfbc = purchase_frequency_by_customer.sort_values(by='len', ascending=False)
print(sorted_pfbc)

#Calculate each customers' purchase amount and sort the purchase values in descending order
purchase_amount_by_customer = data2024.groupby(['CustomerID']).TotalValue.agg([len, min, max])
sorted_pabc = purchase_amount_by_customer.sort_values(by='max', ascending=False)
print(sorted_pabc)

#SalesTrends, line chart
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([107, 96, 96, 94, 86, 86, 80, 78, 77, 70, 69, 57])

plt.plot(x, y)
plt.xlabel("Month")
plt.ylabel("TotalSales")
plt.title("SalesTrends")
plt.legend()
plt.show()

#SalesTrends, heatmap
hmp_trends = np.array([x, y])

plt.figure(figsize=(12, 6))
plt.imshow(hmp_trends, cmap='viridis', interpolation='nearest')

plt.colorbar(label='Count')

plt.title('SalesTrends', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.tight_layout()
plt.legend()
plt.show()

#Total sales by hour, line chart
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
              16, 17, 18, 19, 20, 21, 22, 23])
y = np.array([42, 34, 37, 50, 44, 33, 38, 45, 35, 48, 42, 39, 37, 30, 
              60, 34, 51, 47, 42, 45, 39, 41, 46, 37])

plt.plot(x, y)
plt.xlabel("Hour")
plt.ylabel("TotalSales")
plt.title("Sales by Hour")  
plt.legend()
plt.show()

#Best-selling 10 products by quantity, bar chart 
pd.DataFrame(sales_by_product)
top_10_products_names = ["P059", "P029", "P079", "P062", "P054", "P096", "P022", 
                         "P049", "P048", "P061"]
top_10_products_quantity = sales_by_product.head(10)
plt.figure(figsize=(12, 6)) 
plt.bar(top_10_products_names, top_10_products_quantity, color='skyblue') 
plt.title('Top 10 Best-Selling Products By Quantity') 
plt.xlabel('Product Name') 
plt.ylabel('Total Sales Quantity') 
plt.legend()
plt.show()






