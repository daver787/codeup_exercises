#Create a file named `prepare_zillow.py` that works with the zillow data and does the following:
#1)Removes any properties that are likely to be something other than a single unit property(e.g. no duplexes,no land lot).There are multiple
#ways to estimate that a property is a single unit, and there is not a single "right" answer. You might want to use # bedrooms,
#square feet,unit type or the like to then identify those with unitcnt not defined.

import pandas as pd
from summarize_zillow import nulls_by_col
from summarize_zillow import nulls_by_row

df_zillow_=pd.read_csv("zillow_df.csv")
df_zillow.head()

df_zillow.propertylandusedesc.value_counts()

criteria_1=df_zillow.propertylandusedesc=='Single Family Residential'
criteria_2=df_zillow.unitcnt==1 | df_zillow.unitcnt.isna()

df_zillow=df_zillow[(criteria_1) & (criteria_2)]
df_zillow.shape

#2)handle missing_values(df,prop_required_column,prop_required_row)
#The input:
# A dataframe,a number between 0 and 1 that represents the proportion from each column,of
#rows with non-missing values required to keep the column. i.e. if prop_required_column=.6,then you are requiring
#a column to have at least 60% of values not- NA(no more than 25% missing)

# A dataframe,a number between 0 and 1 that represents the proportion from each row,of
#columnswith non-missing values required to keep the row. i.e. if prop_required_row=.75,then you are requiring
#a row to have at least 75% of values not- NA(no more than 25% missing)

#The output:
#The dataframe with the columns and rows dropped as indicated.Be sure to drop the columns prior to the rows in your function
#hint: look up dropna documentation
#you will want to compute a threshhold from your input values(prop_required)
#make use of inplace arguement


def handle_missing_values(df, prop_required_column, prop_required_row):
    cols_missing = nulls_by_col(df)
    drop_list = list(cols_missing[cols_missing.pct_rows_missing > prop_required_column].index)
    df = df.drop(columns=drop_list)
    rows_missing = nulls_by_row(df)
    df = df[rows_missing.pct_cols_missing > prop_required_row]
    return df
  

#3)Create a function that fills missing values with 0s where it makes sense based on the attribute/field/column/variable

#4)Drop the remaining missing values for the first iteration. Decide if you should drop the rows or the columns. Usually you will base your decision
#1) The number of records it would drop,i.e. the number of missing values in the column, 2) The expected importance of the column

def fill_missing_values(df,fill_value):
    df.fillna(fill_value)
    return df
