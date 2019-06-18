from pydataset import data
import pandas as pd
import numpy as np
#Exercise 1
pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

#Exercise 2
df=data('mpg')

df.shape

df.dtypes

df[df['cty']>df['hwy']]

df['mileage_difference']=df['hwy']-df['cty']

df[['manufacturer','hwy','cty']].groupby('manufacturer').agg(np.mean).sort_values(['hwy','cty'],ascending=False)

df.manufacturer.describe()
len(df.manufacturer.unique())

df.model.describe()
len(df.model.unique())

def convert_trans(column_df):
    if column_df.startswith('auto'):
        return 'auto'
    else:
        return 'manual'

df['trans_fix']=df.trans.apply(convert_trans) 
df.head()       
df[['trans_fix','hwy','cty']].groupby('trans_fix').agg(np.mean)

#Exercise 3
df_1=data('Mammals')

df_1.shape

df_1.dtypes

df_1.nlargest(1,'speed')
df_1[['weight','speed']].sort_values(by='weight',ascending=False)
df_1.specials.mean()*100
len(df_1[(df_1.hoppers==True) &(df_1.speed>df_1.speed.median())])/len(df_1)*100
