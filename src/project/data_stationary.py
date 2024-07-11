import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import df
from statsmodels.tsa.stattools import adfuller


# Checking Stationarity of the Data:
# Rolling Statistic:-

roll_mean=df['Passengers'].rolling(window=2).mean()
roll_std=df['Passengers'].rolling(window=2).std()



# Plot rolling statistics:

plt.figure(figsize=(15,5))
plt.plot(df['Passengers'], color='blue',label='Original')
plt.plot(roll_mean, color='red', label='Rolling Mean')
plt.plot(roll_std, color='black', label='Rolling Std')
plt.title('Rolling Statistics for Mean and Std')
plt.legend(loc='best')
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Time Series/plots/Rolling/roll.png")

# Augmented Dicky Fuller Test:

adf_test=adfuller(df['Passengers'])

# Differencing:

diff=df['Passengers']-df['Passengers'].shift(2)
diff.dropna(inplace=True)

adf_test2=adfuller(diff)


