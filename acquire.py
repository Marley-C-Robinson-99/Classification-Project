import pandas as pd
import os
from env import host, user, password

# Function to establish connection with Codeups MySQL server, drawing username, password, and host from env.py file
def get_db_url(host = host, user = user, password = password, db = 'employees'):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# acquire telco_churn dataset from Codeups MySQL server and cache it to a csv
def get_telco_data():
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM customers', get_db_url(db = 'telco_churn'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)
        # Return the dataframe to the calling code
        return df

# Useful functions to provide high-level overview of the data
def object_vals(df):
    '''
    This is a helper function for viewing the value_counts for object cols.
    '''
    for col, vals in df.iteritems():
        print(df[col].value_counts(dropna = False))

def col_range(df):
    stats_df = df.describe().T
    stats_df['range'] = stats_df['max'] - stats_df['min']
    return stats_df

def summarize_df(df):
    '''
    This function returns the shape, info, a preview, the value_counts of object columns
    and the summary stats for numeric columns.
    '''
    print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('------------------------')
    print('')
    print(df.info())
    print('------------------------')
    print('')
    object_vals(df)
    print('------------------------')
    print('')
    print(col_range(df))