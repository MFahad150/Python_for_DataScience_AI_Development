from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()

# getting data on bitcoin in US Dollar from the past 10 days
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin' , vs_currency='usd', days=10)
# print(bitcoin_data['prices'])

data = pd.DataFrame(bitcoin_data, columns=['TimeStamp', 'Price'])

data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')


# CandleStick Plot (to get the data for daily CandleSticks)
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})



fig = go.Figure(data= [go.Candlestick(x= candlestick_data.index,
                                      open = candlestick_data['Price']['First'],
                                      high = candlestick_data['Price']['max'],
                                      low = candlestick_data['Price']['min'],
                                      close = candlestick_data['Price']['last'])
                                      ])

fig.update_layout(xaxis_rangeslider_visible= False, xaxis_title= 'Date', yaxis_title='Price (USD $)', title='Bitcoin Candlestick Chart Over Past 10 Days')

plot(fig, filename='bitcoin_candlestick_graph.html')