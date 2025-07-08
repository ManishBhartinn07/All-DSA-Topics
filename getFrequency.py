import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dash
from dash import dcc, html

# List of stocks to analyze
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Fetch historical stock data
stock_data = {}
for stock in stocks:
    data = yf.download(stock, period='1y', interval='1d')
    stock_data[stock] = data

# Convert to DataFrame
stock_df = pd.concat(stock_data, names=['Stock', 'Date']).reset_index()

# Calculate Moving Averages
for stock in stocks:
    stock_df.loc[stock_df['Stock'] == stock, '50_MA'] = stock_df.loc[stock_df['Stock'] == stock, 'Close'].rolling(window=50).mean()
    stock_df.loc[stock_df['Stock'] == stock, '200_MA'] = stock_df.loc[stock_df['Stock'] == stock, 'Close'].rolling(window=200).mean()

# Reset index and save data to Excel
stock_df = stock_df.reset_index()
stock_df.to_excel('stock_analysis.xlsx', index=False)

# Visualization with Matplotlib & Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(data=stock_df, x='Date', y='Close', hue='Stock')
plt.title('Stock Price Trends')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(title='Stock')
plt.show()

# Create interactive visualization with Plotly
fig = px.line(stock_df, x='Date', y='Close', color='Stock', title='Stock Price Trends')
fig.show()

# Dash Web App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Stock Price Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
