import matplotlib.pyplot as plt
import numpy as np

# Create a smoother line by taking a moving average
def moving_average(data, window_size=10):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Apply moving average for smoother visualization
smooth_actual_prices = moving_average(actual_prices.flatten(), window_size=5)
smooth_predicted_prices = moving_average(predicted_prices.flatten(), window_size=5)

# Create x-axis range (align with moving average length)
x_range = np.arange(len(smooth_actual_prices))

# Plot Actual vs. Predicted Stock Prices
plt.figure(figsize=(12,6))
plt.plot(x_range, smooth_actual_prices, label='Actual Price', color='green', linewidth=2)
plt.plot(x_range, smooth_predicted_prices, label='Predicted Price', color='red', linestyle='dashed', linewidth=2, alpha=0.8)

# Aesthetics
plt.xlabel('Days')
plt.ylabel('Stock Price (USD)')
plt.title('Actual vs. Predicted Tesla Stock Prices (Smoothed)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Show plot
plt.show()