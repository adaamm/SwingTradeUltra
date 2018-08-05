#Determine the risk level using the VIX_FIX
import datetime as dt
import pandas as pd
import pandas_datareader.data as web

#VixFix = Highest(Close,22) - Low) / (Highest(Close,22)) * 100


def findVixFix(ticker):
    start = dt.datetime(2018,1,1)
    df = web.DataReader(ticker, 'robinhood', start)

    highestClose = df['close_price'].astype(float).tail(22).max()
    low = df['low_price'].astype(float)
    vixFix = (highestClose - low) / (highestClose) * 100
    currentVixFix = vixFix.iloc[-1]

    return currentVixFix
