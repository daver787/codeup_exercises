#Create a file named `summarize_zillow.py` that contains functions that do the following:
#1)Summarizes the data you have just read in to the dataframe in the ways we have discussed
#in previous modules(sample view,datatypes,value counts,summary stats)
#2)Takes in a dataframe and returns a dataframe with thte number of rows and percent
#of rows with missing values for each column.


import pandas as pd

df=pd.read_csv("zillow_df.csv")

#missing values
def nulls_by_col(df):
    num_missing = df.isnull().sum()
    rows = df.shape[0]
    pct_missing = num_missing/rows
    cols_missing = pd.DataFrame({'num_rows_missing': num_missing, 'pct_rows_missing': pct_missing})
    cols_missing.set_index(df.columns)
    return cols_missing

def nulls_by_row(df):
    num_missing = df.isnull().sum(axis=1)
    rows = df.shape[1]
    pct_missing = num_missing/rows
    rows_missing = pd.DataFrame({'num_cols_missing': num_missing, 'pct_cols_missing': pct_missing})
    return rows_missing

#values by category
def df_value_counts(df):
    counts=pd.Series([])
    for col in df.columns.values:
        #print(df[col].dtype)
        if df[col].dtype=='object':
           col_counts=df[col].value_counts()
           counts.append(col_counts)
        #else:
        #col_counts=df[col].value_counts(bins=10,sort=False)
        
    return counts 

def df_summary(df):
    print('--- Shape: {}'.format(df.shape))
    print('--- Info')
    df.info()
    print('--- Descriptions')
    print(df.describe(include='all'))
    print('--- Nulls By Column')
    print(nulls_by_col(df))
    print('--- Nulls By Row')
    print(nulls_by_row(df))
    print('--- Value Counts')
    print(df_value_counts(df))        



