# About Data:-
```
- We are having only 2 columns in our dataset.
- Columns names are : Month and Passengers
-  In Dataset we are having 144 rows.
```

# Cloumns Wise:
## Month:-
```
- Month column is related to date and time.
```

## Passengers:
```
- Passengers column is related to how many people are passing on perticural data and time.
```

# Chesk Trend, Seasonal, Cyclic and Irregularity:-
```
- By applying Line Plot we can able to identify whether our data is Trending or Seasonal or cyclic or Irregular.
- Our data is related to Uptrend.
```

# Stationarity:
## Rolling Statistic:
```
- Applyed rolling statistic technique to to identify whether mean and standard deviation are constant or not.
- I find the mean is not constant.
```
## Augmented Dicky Fuller Test:
```
- Applyed Augmented Dicky Fuller Test to check P-value. which is nothing but applying Hypothesis test.
- In Augmented Dicky Fuller Test is showing p-value is high.
```

# Differencing:-
```
- When i find P-values is high, I applyed Differencing technique to make my data from non-sattionary to stationary data.
```
# ACF & PACF:-
```
- Applyed ACF (Auto Correlation Function) & PACF (Partial Auto Correlation Function) to identify P & Q values.
```
# Slipt Data:-
```
- Slipted data into Train and Test.
```
# Model:-
```
- Applyed ARIMA model which has parameters as (p,d,q). and got Test score is : 0.96 and Train score is : 0.93

Test R2 value : 0.9658014538552823
Train R2 value : 0.9381774545067887
```