import finnhub
import time

print("Enter Finnhub API Key:", end='')
FINNHUB_API_KEY = input()

finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
DSC = 86400  #DAY SECONDS CONST
HOUR = 3600  #HOUR SECONDS CONST


def get_stock_candles(acronym, time_period):
    if (time_period == 'd'):
        res = finnhub_client.stock_candles(symbol=acronym,
                                           resolution='1',
                                           _from=int(time.time()-(DSC)),
                                           to=int(time.time())
                                           )
    elif (time_period == 'w'):
        res = finnhub_client.stock_candles(symbol=acronym,
                                           resolution='1',
                                           _from=int(time.time()-(DSC*7)),
                                           to=int(time.time())
                                           )
    elif (time_period == 'm'):
        res = finnhub_client.stock_candles(symbol=acronym,
                                           resolution='1',
                                           _from=int(time.time()-(DSC*30)),
                                           to=int(time.time())
                                           )
    elif (time_period == 'y'):
        res = finnhub_client.stock_candles(symbol=acronym,
                                           resolution='1',
                                           _from=int(time.time()-(DSC*365)),
                                           to=int(time.time())
                                           )
    else:
        res = finnhub_client.stock_candles(symbol=acronym,
                                            resolution='1',
                                            _from=int(time.time()-(HOUR*int(time_period))),
                                            to=int(time.time())
                                            )
    return res




def get_quote(acronym):
    QUOTE = finnhub_client.quote(acronym)
    curr_price = QUOTE['c']
    delta = curr_price - QUOTE['pc']
    percent_change = '{:+.2f}%'.format((delta/QUOTE['pc'])*100)

    return (curr_price, '{:+.2f}'.format(delta), percent_change)

res = finnhub_client.stock_candles(symbol='NVDA',
                                    resolution='1',
                                    _from=int(time.time()-(DSC)),
                                    to=int(time.time()-300)
                                    )

import pandas as pd
import plotly.graph_objects as go
import plotly


def plot_stock_data(res):
    data_frame = pd.DataFrame(res)
    data_frame['t'] = pd.to_datetime(data_frame['t'], unit='s')
    
    
    data = [go.Candlestick(x=data_frame['t'],
            open=data_frame['o'],
            high=data_frame['h'],
            low=data_frame['l'],
            close=data_frame['c'],
            increasing_line_color="mediumseagreen",
            decreasing_line_color="maroon")]

    figSignal = go.Figure(data=data)
    figSignal.update_layout(xaxis_rangeslider_visible=False,
                        margin=dict(l=0, r=0, t=0, b=0),
                        plot_bgcolor='#36393f',
                        paper_bgcolor='#36393f',
                        yaxis=dict(color='#8F97A6'),
                        xaxis=dict(color='#8F97A6')
                        )
    figSignal.update_xaxes(linecolor='#40444B', gridcolor='#40444B')
    figSignal.update_yaxes(linecolor='#40444B', gridcolor='#40444B')

    figSignal.write_image("fig1.png")
