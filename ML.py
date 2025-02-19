# Extract relevant features
data = df[['Date', 'Close/Last']]

# Normalize data using MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data[['Close/Last']])

# Define function to create sequences for LSTM
def create_sequences(data, time_steps=60):
    X, y = [], []
    for i in range(time_steps, len(data)):
        X.append(data[i-time_steps:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)

# Create sequences
time_steps = 60
X, y = create_sequences(scaled_data, time_steps)

# Reshape input data for LSTM model
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)