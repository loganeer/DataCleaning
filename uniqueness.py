import pandas as pd

# Create a sample dataset
data = {
    'Email': ['john.doe@example.com', 'jane.smith@example.com', 
    'james.doe@example.com', 'john.doe@example.com', 'susan.brown@example.com'],
}
df = pd.DataFrame(data)

# Check uniqueness and create a Boolean mask for duplicated email addresses
duplicated_mask = df['Email'].duplicated(keep='first')
# Create a new column to indicate uniqueness
df['Uniqueness'] = ~duplicated_mask

unique_percentage = (df['Uniqueness'].sum() / len(df)) * 100

print(df)