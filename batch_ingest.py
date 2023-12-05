import s3fs
from s3fs.core import S3FileSystem
from kaggle.api.kaggle_api_extended import KaggleApi
import pickle
import pandas as pd

def ingest_data():
    api = KaggleApi()
    api.authenticate()
    # Load the rice, wheat, and corn prices dataset from a CSV file
    # Specify the full path to download the file
    # download single file
    # Signature: dataset_download_file(dataset, file_name, path=None, force=False, quiet=True)
    api.dataset_download_file('timmofeyy/-cerial-prices-changes-within-last-30-years', 'rice_wheat_corn_prices.csv')
    rwc_prices_data = pd.read_csv('rice_wheat_corn_prices.csv')
    print(rwc_prices_data)

    # Adding noise to the Data to simulate a noisy dataset (You can adjust these steps accordingly)
    # Here, I'm adding NaN values, outliers, and duplicate values as an example
    for col in rwc_prices_data.columns:
        rwc_prices_data.loc[rwc_prices_data.sample(frac=0.001).index, col] = None

    rand_col = 'Year'  # You can choose a random column or create a new one if needed
    rwc_prices_data.loc[rwc_prices_data.sample(frac=0.005).index, rand_col] = 1000
    rwc_prices_data.loc[rwc_prices_data.sample(frac=0.005).index, rand_col] = 0

    rwc_prices_data = pd.concat([rwc_prices_data, rwc_prices_data.sample(frac=0.005)])

    # Push the data to S3 bucket as a pickle file
    s3 = S3FileSystem()
    # S3 bucket directory
    DIR = 's3://ece5984-bucket-abdulmaj/Final-Project'  # Enter your S3 directory
    with s3.open(f'{DIR}/rwc_prices_data.pkl', 'wb') as f:
         f.write(pickle.dumps(rwc_prices_data))

ingest_data()