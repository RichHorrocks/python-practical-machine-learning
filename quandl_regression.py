import pandas as pd
import quandl
import math

# Get the data frame. (i.e. The dataset.)
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]

# Define a new column that gives us the percentage change between high and low.
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100

# Define a new column that gives us the precentage change between open and close.
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

# Define our features.
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
# Fill in any values that aren't available. Here we have to replace the NaN data
# with something.
df.fillna(-99999, inplace=True)

# Round everything to the nearest whole. Forecast out 10% by using data from
# the previous 10 days to predict today.
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())
print(df.tail())
