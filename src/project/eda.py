import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df


class eda:

    try:

        eda_null=df.isnull().sum()
        eda_dup=df.duplicated().sum()

    except Exception as e:
        raise Exception(f"Error find in eda :\n"+str(e))

    def __init__(self,eda_null,eda_dup):

        try:
            
            self.eda_null=eda_null
            self.eda_dup=eda_dup

        except Exception as e:
            raise Exception(f"Error in initialization :\n"+str(e))
        
    try:

        def eda_null_defin(self):
            return self.eda_null
        
        def eda_dup_defin(self):
            return self.eda_dup
        
    except Exception as e:
        raise Exception(f"Error find in eda define level :\n"+str(e))
    

fig,ax=plt.subplots(figsize=(10,5))
sns.lineplot(x=df.index,y=df['Passengers'])
plt.title('Checking Trend, Seasonal, Cyclic,and Irregularity :')
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Time Series/plots/check_trend/trend.png")

    