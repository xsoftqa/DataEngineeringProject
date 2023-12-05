import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle

def transform_data():

    s3 = S3FileSystem()
    # S3 bucket directory (data lake)
    DIR = 's3://ece5984-bucket-abdulmaj/Final-Project'                                  # Insert here
    # Get data from S3 bucket as a pickle file
    raw_data = np.load(s3.open('{}/{}'.format(DIR, 'rwc_prices_data.pkl')), allow_pickle=True)     # insert here

    #raw_data = np.load('data.pkl', allow_pickle=True)
    # Dividing the raw dataset for each company individual company
    raw_data.columns = raw_data.columns.swaplevel(0,1)
    raw_data.sort_index(axis=1, level=0, inplace=True)
    df_rice_rw = raw_data['RICE']
    df_wheat_rw = raw_data['WHEAT']
    df_corn_rw = raw_data['CORN']

    # Dropping rows with NaN in them
    df_rice = df_rice_rw.dropna()
    df_wheat = df_wheat_rw.dropna()
    df_corn = df_corn_rw.dropna()

    # Removing rows with outliers
    for col in list(df_rice.columns)[0:8]:                                          # We ignore 'Volume' column
        df_rice = df_rice.drop(df_rice[df_rice[col].values > 900].index)            # Values above 900 are dropped
        df_rice = df_rice.drop(df_rice[df_rice[col].values < 0.001].index)          # Values below 0.001 are dropped

        df_wheat = df_wheat.drop(df_wheat[df_wheat[col].values > 900].index)
        df_wheat = df_wheat.drop(df_wheat[df_wheat[col].values < 0.001].index)

        df_corn = df_corn.drop(df_corn[df_corn[col].values > 900].index)
        df_corn = df_corn.drop(df_corn[df_corn[col].values < 0.001].index)

    # Dropping duplicate rows
    df_rice = df_rice.drop_duplicates()
    df_wheat = df_wheat.drop_duplicates()
    df_corn = df_corn.drop_duplicates()

    # Push cleaned data to S3 bucket warehouse
    DIR_wh = 's3://ece5984-bucket-abdulmaj/Final-Project/CLEANED-DATA'                     # Insert here
    with s3.open('{}/{}'.format(DIR_wh, 'clean_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(df_rice))
    with s3.open('{}/{}'.format(DIR_wh, 'clean_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(df_wheat))
    with s3.open('{}/{}'.format(DIR_wh, 'clean_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(df_corn))



