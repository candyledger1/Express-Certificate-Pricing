

### IMPORTS

import numpy as np
import pandas as pd
import yfinance as yf
from pandas_datareader import data


### DOWNLOAD DATA

def download_stock_price_data(tickers, start_date, end_date):    
    # download the time series of adj. close price 
    # for each of the tickers from Yahoo finance
    # and dataframe with price changes
    #
    # in case you receive an error update your yfinance to the current version
    # and/or perform bug fixing
    
    df_prices = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)['Close']
    prev = df_prices.to_numpy()
    prev = prev / np.insert(prev[:-1,:], 0, np.ones(prev.shape[1]), 0)
    prev[0] = np.ones(prev.shape[1])
    df_price_changes = df_prices.copy(deep=True)
    df_price_changes[:] = prev

    return df_prices, df_price_changes


