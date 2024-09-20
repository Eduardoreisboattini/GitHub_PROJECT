import pandas as pd  # Importing Pandas library

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df_pandas = pd.DataFrame(data)  # Creating a DataFrame using Pandas

# Display the DataFrame
print("Pandas DataFrame:")
print(df_pandas)

# Filter rows where Age is greater than 30
filtered_df = df_pandas[df_pandas['Age'] > 30]  # Filtering using boolean indexing
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Calculate the average age
average_age = df_pandas['Age'].mean()  # Calculating the mean of the 'Age' column
print("\nAverage Age:", average_age)
