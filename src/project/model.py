import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from acf_pacf import y_train,y_test
from data_stationary import diff
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf,pacf
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import r2_score
import warnings
warnings.simplefilter('ignore')



arima_model=ARIMA(diff,order=(11,0,12))
arima=arima_model.fit()
y_pre_test=arima.predict(start=y_test.index[0],end=y_test.index[-1])
y_pre_train=arima.predict(start=y_train.index[0],end=y_train.index[-1])

