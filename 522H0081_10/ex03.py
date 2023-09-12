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

