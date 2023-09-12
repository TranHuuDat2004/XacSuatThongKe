import pandas as pd

# Read dataset population from file population.csv
data = pd.read_csv("population.csv", delimiter=',')

# Show the first 5 data points
print(data.head(5))

# Compute the count, mean, standard deviation, minimum, and maximum values by year
result = data.groupby(['Country Name', 'Country Code'])['Value'].agg(['count', 'mean', 'std', 'min', 'max']).reset_index()

# Add the desired columns to the result dataframe
result['Mean'] = result['mean']
result['Std'] = result['std']
result['Min'] = result['min']
result['Max'] = result['max']

# Reorder the columns
result = result[['Country Name', 'Country Code', 'Mean', 'Std', 'Min', 'Max']]

# Display the result
print(result)
