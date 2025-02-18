import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Step 1: Load Real Tesla Stock Price Data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
    df['Close/Last'] = df['Close/Last'].replace('[\$,]', '', regex=True).astype(float)
    return df

# Step 2: Predict Future Stock Prices
def predict_future_prices(df, end_date):
    start_date = df['Date'].max() + timedelta(days=1)
    future_dates = pd.date_range(start=start_date, end=end_date, freq='B')
    
    np.random.seed(42)
    initial_price = df['Close/Last'].iloc[-1]
    price_series = [initial_price]
    
    for _ in range(len(future_dates)):
        daily_return = np.random.normal(loc=0.001, scale=0.02)
        spike = np.random.choice([0, np.random.normal(0.03, 0.02)], p=[0.95, 0.05])
        new_price = price_series[-1] * (1 + daily_return + spike)
        price_series.append(new_price)
    
    predicted_prices = pd.Series(price_series[1:], index=future_dates)
    return predicted_prices

# Step 3: Create visualization with clean 50-unit intervals
def create_stock_prediction_plot(df, predicted_prices):
    plot_df = pd.concat([df.set_index('Date')['Close/Last'], predicted_prices], axis=0)
    fig = go.Figure()
    
    # Historical prices
    fig.add_trace(go.Scatter(
        x=plot_df.index[:len(df)],
        y=plot_df.values[:len(df)],
        mode='lines',
        name='Tesla Stock Price',
        line=dict(color='royalblue', width=2)
    ))
    
    # Predicted Prices with Color Changes
    predicted_values = plot_df.values[len(df):]
    predicted_dates = plot_df.index[len(df):]
    colors = ['green' if predicted_values[i] >= predicted_values[i-1] else 'red' 
              for i in range(1, len(predicted_values))]
    colors.insert(0, 'green')
    
    for i in range(len(predicted_dates)-1):
        fig.add_trace(go.Scatter(
            x=predicted_dates[i:i+2],
            y=predicted_values[i:i+2],
            mode='lines',
            line=dict(color=colors[i], width=2),
            showlegend=False
        ))
    
    # Calculate y-axis range with clean 50-unit intervals
    all_values = np.concatenate([plot_df.values[:len(df)], predicted_values])
    min_price = 0  # Start from 0
    max_price = np.ceil(max(all_values) / 50) * 50  # Round up to nearest 50
    
    fig.update_layout(
        title="Tesla Stock Price Over Time",
        xaxis_title="Date",
        yaxis_title="Stock Price (USD)",
        template="plotly_dark",
        hovermode="x unified",
        showlegend=True,
        height=600,
        width=1200,
        margin=dict(l=50, r=50, t=50, b=50),
        yaxis=dict(
            range=[min_price, max_price],
            tickmode='linear',
            tick0=0,
            dtick=50,  # Set ticks every 50 units
            autorange=False,
            gridwidth=1,
            gridcolor='rgba(128, 128, 128, 0.2)',
            zeroline=False
        )
    )
    return fig

# Step 4: Main function
def main():
    file_path = "/Users/sreevarshansathiyamurthy/Downloads/HistoricalData_1739813801084.csv"
    df = load_data(file_path)
    end_date = datetime(2025, 12, 31)
    predicted_prices = predict_future_prices(df, end_date)
    fig = create_stock_prediction_plot(df, predicted_prices)
    fig.show()

if __name__ == "__main__":
    main()