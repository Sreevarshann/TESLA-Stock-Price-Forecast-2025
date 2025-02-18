# Check for missing values
print(df.isnull().sum())

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort data by date
df = df.sort_values(by='Date')

# Convert necessary columns to numeric (if needed)
df['Close/Last'] = df['Close/Last'].replace('[\$,]', '', regex=True).astype(float)

# Display cleaned data
df.head()