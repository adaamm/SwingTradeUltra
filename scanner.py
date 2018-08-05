import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from pyfiglet import figlet_format

print(figlet_format('Swing Trade Ultra'))

style.use('ggplot')

ticker = input("Please enter a Stock Symbol: ")
#Converts all ticker symbols to uppercase so that Robinhoods API can recognize it
ticker = ticker.upper()
#Set data-frame to the specified dates
start = dt.datetime(2018,1,1)
df = web.DataReader(ticker, 'robinhood', start)
                #df = df.iloc[::-1]
                #df = pd.read_csv('CVSInfo.csv', parse_dates = True, index_col = 0)

#Calculate CCI
#CCI = (Typical Price - 20-period SMA of TP) / (0.015 x Mean Deviation)
#Typical Price = (High + Low + CLose)/3
df['TP'] = (df['close_price'].astype(float) + df['high_price'].astype(float) + df['low_price'].astype(float)) / 3
#20-Day SMA
df['20sma'] = df['close_price'].astype(float).rolling(window=20,min_periods=0).mean()
#Mean Deviation
df['MD'] = df['20sma'].iloc[-1] - df['TP']
df['MD'] = abs(df['MD'])
df['MD'] = (df['MD'].tail(20).sum()) / 20
#Constant
constant = 0.015
#CCI
df['CCI'] = (df['TP'] - df['20sma']) / (constant * df['MD'])
print('\n')
currentCCI = df['CCI'].iloc[-1];
if currentCCI <= -100:
    print("{} is potentially being set-up for a breakout, watch for a CCI cross of [-100] for confirmation".format(ticker))
elif currentCCI > -100 and currentCCI < 0:
    print("{} is potentially being set-up for a breakout, watch for a CCI cross of [0] for confirmation".format(ticker))
elif currentCCI >= 100:
    print("{} has high momentum but is nearing the upwards trajectory of it's cycle, watch for a cross from above [100] for confirmation of downtrend".format(ticker))
else:
    print("{} is not a good swing trade buy opportunity ".format(ticker))


#df['AdjClose'].plot()
#FIX
#lastDate = df['begins_at'].iloc[-1].astype(string)
print('\nThe last recorded CCI was {}, on {}'.format(currentCCI, 'NULL'))
print('\n\n\n\n\nMarket Data provided by: {}'.format('Robinhood'))
print('\nProgramed using Python, pandas, pandas_datareader')
print('\nBy: Yong Chong 2018')
print('\nDisclaimer: Not professional financial or investment advice')
df.to_csv('CVSInfo.csv')
#plt.show()
