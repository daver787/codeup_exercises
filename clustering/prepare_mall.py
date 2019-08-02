#Create a file named `prepare_mall.py` that contains functions that do the following:
#detects any outliers
#encodes all the categorical columns(of non-numeric data types), and adds the encoded
#column(i.e. it doesnt remove the original column)
#accepts the unprepared mall customers data frame and applies all the transformations above
from aquire_mall import get_connection
from aquire_mall import get_mall_data

#get mall data
mall_df=get_mall_data()

#find the outliers
def get_upper_outliers(s, k):
    '''
    Given a series and a cutoff value, k, returns the upper outliers for the
    series.

    The values returned will be either 0 (if the point is not an outlier), or a
    number that indicates how far away from the upper bound the observation is.
    '''
    q1, q3 = s.quantile([.25, .75])
    iqr = q3 - q1
    upper_bound = q3 + k * iqr
    return s.apply(lambda x: max([x - upper_bound, 0]))

def get_lower_outliers(s, k):
    '''
    Given a series and a cutoff value, k, returns the upper outliers for the
    series.

    The values returned will be either 0 (if the point is not an outlier), or a
    number that indicates how far away from the upper bound the observation is.
    '''
    q1, q3 = s.quantile([.25, .75])
    iqr = q3 - q1
    lower_bound = q1 - k * iqr
    return s.apply(lambda x: min([x-lower_bound, 0]))   


def add_outlier_columns(df, k):
    '''
    Add a column with the suffix _outliers for all the numeric columns
    in the given dataframe.
    '''
    # outlier_cols = {col + '_outliers': get_upper_outliers(df[col], k)
    #                 for col in df.select_dtypes('number')}
    # return df.assign(**outlier_cols)

    for col in df.select_dtypes('number'):
        df[col + '_outliers_u'] = get_upper_outliers(df[col], k)
        df[col+'outliers_l']=get_lower_outliers(df[col],k)

    return df



add_outlier_columns(mall_df, k=1.5)


outlier_cols = [col for col in mall_df if col.endswith(('_outliers_l','_outliers_u'))]
for col in outlier_cols:
    print('~~~\n' + col)
    data = mall_df[col][mall_df[col] > 0]
    print(data.describe())


#Encode all the object columns if neccesary
def encode_df(df):
 for col in df.select_dtypes('object'):
  encoder=LabelEncoder()
  encoder.fit(col)
  df[col+'_encode']=encoder.transform(col)
 return df


 #accepts the unprepared mall customers dataframe and applies all the transformation above
def transform_mall(df,k):
    df=add_outlier_columns(df,k)
    df=encode_df(df)
    return df
 