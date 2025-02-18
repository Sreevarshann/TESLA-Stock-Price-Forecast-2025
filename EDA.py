import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Add trace for historical stock prices
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Close/Last'], 
    mode='lines',
    name='Tesla Stock Price',
    line=dict(color='royalblue', width=3)
))

# Customize layout
fig.update_layout(
    title="Tesla Stock Price Over Time",
    xaxis_title="Date",
    yaxis_title="Stock Price (USD)",
    template="plotly_dark",
    hovermode="x unified",
    showlegend=True
)

# Show interactive chart
fig.show()