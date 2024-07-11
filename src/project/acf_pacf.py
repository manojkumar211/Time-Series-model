import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_stationary import diff
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf,pacf
import statsmodels.api as sm

fig=sm.graphics.tsa.plot_acf(diff,lags=40)
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Time Series/plots/acf_pacf/acf.png")
fig=sm.graphics.tsa.plot_pacf(diff,lags=40)
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Time Series/plots/acf_pacf/pacf.png")


y_train=diff[:114]
y_test=diff[114:]

