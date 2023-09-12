import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Read iris.csv
data = pd.read_csv("iris.csv")

# Convert the data column to numeric type
data['sepal_length'] = pd.to_numeric(data['sepal_length'], errors='coerce') # hàm errors='coerce' biến dữ liêu này thành NaN (Not a Number)

# Task 2: Plot a simple scatter of sepal_length vs sepal_width
plt.scatter(data['sepal_length'], data['sepal_width'])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.title('Scatter Plot: Sepal Length vs Sepal Width')
plt.show()

# Task 3: Show the histogram of sepal_length with 20 bins
plt.hist(data['sepal_length'], bins=20)
plt.xlabel('sepal_length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.show()
