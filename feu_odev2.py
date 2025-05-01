# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:33:46 2025

@author: Elif
"""

#COLUMN DESCRIPTIONS
#Date: The date of the sale (in YYYY-MM-DD format). 
#Category: The category of the product (e.g., Electronics, Furniture, Fashion). 
#Product: The name of the sold product. 
#Quantity: The number of units sold. 
#Price: The unit price of the product (in local currency). 

#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Preparing the dataset to examine, then examine with info and describe
file_path = "C:\\Users\\Elif\\Downloads\\sales_data.csv"
data113 = pd.read_csv(file_path)
print(data113.head(10))
print(data113.info())
print(data113.describe())

#Cleaning the data, using datetime, and preparing a month column for further analysis
data113.dropna(inplace = True)
data113['Date'] = pd.to_datetime(data113['Date'])
data113['Month'] = data113['Date'].dt.month
print(data113)

#Calculations and adding the "Total_Sales" column for each sale
data113['Total_Sales'] = data113['Quantity'] * data113['Price']

#Analyzing annual total sales quantity by category
total_sales_quantity_by_category = data113.groupby(['Category']).Quantity.agg([len])
sorted_tsqbc = total_sales_quantity_by_category.sort_values(by='len', ascending=False)
print(sorted_tsqbc)
#The category "furniture" was the best selling category

#Analyzing annual total sales revenue by category
total_revenue_by_category = data113.groupby(['Category']).Total_Sales.sum()
sorted_trbc = total_revenue_by_category.sort_values
print(sorted_trbc)

#Analyzing monthly total sales quantity and revenue
total_quantity_sold_by_month = data113.groupby(['Month']).Quantity.sum()
sorted_tqsbm = total_quantity_sold_by_month.sort_values(ascending=False)
print(sorted_tqsbm)

total_revenue_by_month = data113.groupby(['Month']).Total_Sales.sum()
sorted_trbm = total_revenue_by_month.sort_values(ascending=False)
print(sorted_trbm)
#December was the month with the highest revenue.

#Table showing the total quantity sold and total revenue for each month
monthly_summary = data113.groupby('Month').agg(
    Total_Revenue=('Total_Sales', 'sum'),
    Total_Quantity=('Quantity', 'sum')
).reset_index()

print(monthly_summary)

#Total Monthly Sales Revenue, line chart
plt.plot(total_revenue_by_month.index.astype(str), total_revenue_by_month)
plt.xlabel("Month")
plt.ylabel("Total Sales Revenue")
plt.title("Total Monthly Sales Revenue")  
plt.show()
#This chart shows that we sell things in April and December more, which makes 
#spring and winter the best selling seasons. I suggest a further analysis about
#product-season based sales.


#The Share of Total Revenue by Product Category, pie chart
plt.pie(
    total_revenue_by_category, 
    labels=total_revenue_by_category.index, 
    startangle=140, 
    colors=plt.cm.Paired.colors
)
plt.title('Share of Total Revenue by Product Category')
plt.show()


#Top 10 Products by Quantity, bar chart
top10_products = data113.groupby(['Product']).Quantity.sum().head(10) 
plt.bar(top10_products.index, top10_products, color='skyblue') 
plt.title('Top 10 Best-Selling Products By Quantity') 
plt.xlabel('Product') 
plt.ylabel('Annual Sales Quantity') 
plt.show()



















