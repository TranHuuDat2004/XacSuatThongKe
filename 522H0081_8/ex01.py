import pandas as pd

# Read the dataset from the CSV file
data = pd.read_csv("iris.csv")

# Show the first 5 data points
print(data.head(5))

# Convert the data column to numeric type
data['sepal_length'] = pd.to_numeric(data['sepal_length'], errors='coerce') # hàm errors='coerce' biến dữ liêu này thành NaN (Not a Number)

# Compute the count
count = len(data)

# Compute the mean
mean = data['sepal_length'].sum() / count

# Compute the standard deviation
variance = sum((x - mean) ** 2 for x in data['sepal_length']) / count
std = variance ** 0.5

# Compute the minimum and maximum
minimum = data['sepal_length'].min()
maximum = data['sepal_length'].max()

# Create a DataFrame to show the results
result = pd.DataFrame({
    'Count': [count],
    'Mean': [mean],
    'Standard Deviation': [std],
    'Min': [minimum],
    'Max': [maximum]
})

# Display the result
print(result)

