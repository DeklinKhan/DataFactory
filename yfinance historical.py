# -*- coding: utf-8 -*-
import yfinance as yf
import pandas as pd


labels = ["BTC-USD","BNB-USD", "DOGE-USD", "ETH-USD", "LTC-USD", "XRP-USD","USDT-USD","HEX-USD","SHIB-USD"]
dataframe = pd.DataFrame(columns=["Open", "High", "Low", "Close","Volume"])
for i in labels:
    Ticker = yf.Ticker(i)
    df = pd.DataFrame(Ticker.history(period = "10y", interval="1d"))
    df1 = df[["Open", "High", "Low", "Close"]]
    df2 = df[["Close","Volume"]]
    print(df2)
    df1.to_csv(i + 'candle.csv')
    df2.to_csv(i + 'volume.csv')
