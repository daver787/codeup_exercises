import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


from acquire import get_titanic_data

df = get_titanic_data()
df.embark_town.fillna('Other', inplace=True)
df.drop(columns=['deck'], inplace=True)

encoder = LabelEncoder()
df.embarked.fillna('Unknown', inplace=True)
encoder.fit(df.embarked)
df.embarked = encoder.transform(df.embarked)

from sklearn.model_selection import train_test_split

train, test = train_test_split(
    df, test_size=.30, random_state=123, stratify=df.survived)


scaler = MinMaxScaler()
scaler.fit(train[['age', 'fare']])
train[['age', 'fare']] = scaler.transform(train[['age', 'fare']])
test[['age', 'fare']] = scaler.transform(test[['age', 'fare']])    
