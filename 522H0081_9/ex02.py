import pandas as pd
import matplotlib.pyplot as plt

# Read the data from company_sales_data.csv
data = pd.read_csv("company-sales_data.csv")

# Task 1: Line plot for total profit of all months
months = data['month_number']
total_profit = data['total_profit']
plt.plot(months, total_profit, marker='o')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.title('Total Profit of All Months')
plt.grid()
plt.show()

# Task 2: Scatter plot for toothpaste sales data
toothpaste_sales = data['toothpaste']
plt.scatter(months, toothpaste_sales)
plt.xlabel('Month')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales by Month')
plt.grid()
plt.show()

# Task 3: Bar chart for facecream and facewash sales data
facecream_sales = data['facecream']
facewash_sales = data['facewash']

plt.bar(months, facecream_sales, label='Facecream', width=0.4)
plt.bar(months, facewash_sales, label='Facewash', width=0.4, align='edge')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Facecream and Facewash Sales by Month')
plt.legend()
plt.grid()
plt.show()
