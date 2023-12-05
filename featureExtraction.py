import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import TimeSeriesSplit


def feature_extract():

    s3 = S3FileSystem()
    # S3 bucket directory (data warehouse)
    DIR_wh = 's3://ece5984-bucket-abdulmaj/Final-Project/CLEANED-DATA'                        # Insert here
    # Get data from S3 bucket as a pickle file
    rice_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_rice.pkl')), allow_pickle=True)
    wheat_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_wheat.pkl')), allow_pickle=True)
    corn_df = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_corn.pkl')), allow_pickle=True)

    # Load pickle data locally
    # aapl_df = np.load('clean_aapl.pkl', allow_pickle=True)
    # amzn_df = np.load('clean_amzn.pkl', allow_pickle=True)
    # googl_df = np.load('clean_googl.pkl', allow_pickle=True)

    # Set Target Variable
    target_rice = pd.DataFrame(rice_df['Year'])
    target_wheat = pd.DataFrame(wheat_df['Year'])
    target_corn = pd.DataFrame(corn_df['Year'])
    # Selecting the Features
    features = ['Year', 'Month', 'Price_wheat_ton', 'Price_rice_ton', 'Price_corn_ton', 'Inflation_rate', 'Price_wheat_ton_infl', 'Price_rice_ton_infl', 'Price_corn_ton_infl']

    # feature extraction on the RICE prediction on future prices dataset
    # Scaling RICE dataframe
    scaler = MinMaxScaler()
    feature_transform_rice = scaler.fit_transform(rice_df[features])
    feature_transform_rice = pd.DataFrame(columns=features, data=feature_transform_rice, index=rice_df.index)

    # Splitting to Training set and Test set
    timesplit = TimeSeriesSplit(n_splits=10)
    for train_index, test_index in timesplit.split(feature_transform_rice):
        X_train, X_test = feature_transform_rice[:len(train_index)], feature_transform_rice[len(train_index): (len(train_index)+len(test_index))]
        y_train, y_test = target_rice[:len(train_index)].values.ravel(), target_rice[len(train_index): (len(train_index)+len(test_index))].values.ravel()

    # Push extracted features to data warehouse
    DIR_rice = 's3://ece5984-bucket-abdulmaj/Final-Project/RICE-DW'                   # Insert here
    with s3.open('{}/{}'.format(DIR_rice, 'X_train_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_rice, 'X_test_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_rice, 'y_train_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR_rice, 'y_test_rice.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))

    # feature extraction on the WHEAT prediction on future prices dataset
    # Scaling WHEAT dataframe
    scaler = MinMaxScaler()
    feature_transform_wheat = scaler.fit_transform(wheat_df[features])
    feature_transform_wheat = pd.DataFrame(columns=features, data=feature_transform_wheat, index=wheat_df.index)

    # Splitting to Training set and Test set
    timesplit = TimeSeriesSplit(n_splits=10)
    for train_index, test_index in timesplit.split(feature_transform_wheat):
        X_train, X_test = feature_transform_wheat[:len(train_index)], feature_transform_wheat[len(train_index): (len(train_index)+len(test_index))]
        y_train, y_test = target_wheat[:len(train_index)].values.ravel(), target_wheat[len(train_index): (len(train_index)+len(test_index))].values.ravel()

    # Push extracted features to data warehouse
    DIR_wheat = 's3://ece5984-bucket-abdulmaj/Final-Project/WHEAT-DW'                               # Insert here
    with s3.open('{}/{}'.format(DIR_wheat, 'X_train_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_wheat, 'X_test_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_wheat, 'y_train_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR_wheat, 'y_test_wheat.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))

    # feature extraction on the CORN prediction on future prices dataset
    # Scaling CORN dataframe
    scaler = MinMaxScaler()
    feature_transform_corn = scaler.fit_transform(corn_df[features])
    feature_transform_corn = pd.DataFrame(columns=features, data=feature_transform_corn, index=corn_df.index)

    # Splitting to Training set and Test set
    timesplit = TimeSeriesSplit(n_splits=10)
    for train_index, test_index in timesplit.split(feature_transform_corn):
        X_train, X_test = feature_transform_corn[:len(train_index)], feature_transform_corn[len(train_index): (len(train_index)+len(test_index))]
        y_train, y_test = target_corn[:len(train_index)].values.ravel(), target_corn[len(train_index): (len(train_index)+len(test_index))].values.ravel()

    # Push extracted features to data warehouse
    DIR_corn = 's3://ece5984-bucket-abdulmaj/Final-Project/CORN-DW'                 # Insert here
    with s3.open('{}/{}'.format(DIR_corn, 'X_train_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_corn, 'X_test_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_corn, 'y_train_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR_corn, 'y_test_corn.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))




