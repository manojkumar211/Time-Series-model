import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("C:/AI&ML Engineer/Projects/Apple/Time Series/AirPassengers.csv")

class data:

    try:

        df_head=df.head()
        df_tail=df.tail()
        df_des=df.describe()
        df_colmn=df.columns
        df_null=df.isnull().sum()
        df_dup=df.duplicated().sum()

    except Exception as e:
        raise Exception(f"Error find in data :\n" + str(e))

    def __init__(self, df_head, df_tail, df_des, df_colmn, df_null, df_dup):

        try:

            self.df_head = df_head
            self.df_tail = df_tail
            self.df_des = df_des
            self.df_colmn = df_colmn
            self.df_null = df_null
            self.df_dup = df_dup

        except Exception as e:
            raise Exception(f"Error in initialization :\n" + str(e))
        
    try:

        def df_head_defin(self):
            return self.df_head
        
        def df_tail_defin(self):
            return self.df_tail
        
        def df_des_defin(self):
            return self.df_des
        
        def df_colmn_defin(self):
            return self.df_colmn
        
        def df_null_defin(self):
            return self.df_null
        
        def df_dup_defin(self):
            return self.df_dup
    
    except Exception as e:
        raise Exception(f"Error in getter methods :\n" + str(e))
    

    