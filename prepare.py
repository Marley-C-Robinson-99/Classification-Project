import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Hist plot distribution for all non-object columns
def num_distributions(df):
    '''
    This functions takes in a dataframe and displays
    the distribution of each numeric column.
    '''
    # for col in df.columns:
    #     if df[col].dtype != 'object':
    #         plt.hist(df[col])
    #         plt.title(f'Distribution of {col}')
    #         plt.show()
    for col, vals in df.iteritems():
        if df[f'{col}'].dtype != object:
            print(df[f'{col}'].value_counts(), sns.histplot(data = df[f'{col}']), plt.title(f'Distribution of {col}'),
            plt.show(), end = '\n------------------------------------\n')

# Prepare telco data for use in an algorithm by encoding, dropping, and creating dummies
def prep_telco(df):
    '''
    This function take in the telco data acquired by get_telco_data,
    Returns prepped train, validate, and test dfs with dropped `unnamed: 0` and `customer_id`
    as well as dropping duplicates and encoding columns so as to be readable by an algorithm
    '''
    # drop the duplicates, customer_id, and Unnamed: 0 columns
    df.drop_duplicates(inplace = True)
    df.drop(columns = {'customer_id'}, inplace = True)

    # encoding columns containing strings
    df['gender'] = df['gender'].replace(['Female', 'Male'], [0,1])
    df['partner'] = df['partner'].replace(['No', 'Yes'], [0,1])
    df['dependents'] = df['dependents'].replace(['No', 'Yes'], [0,1])
    df['phone_service'] = df['phone_service'].replace(['No', 'Yes'], [0,1])
    df['multiple_lines'] = df['multiple_lines'].replace(['No phone service','No', 'Yes'], [0, 0 ,1])
    df['online_security'] = df['online_security'].replace(['No internet service', 'No', 'Yes'], [0,0,1])
    df['online_backup'] = df['online_backup'].replace(['No internet service', 'No', 'Yes'], [0,0,1])
    df['device_protection'] = df['device_protection'].replace(['No internet service', 'No', 'Yes'], [0,0,1])
    df['tech_support'] = df['tech_support'].replace(['No internet service', 'No', 'Yes'], [0,0,1])
    df['streaming_tv'] = df['streaming_tv'].replace(['No internet service', 'No', 'Yes'], [0,0,1])
    df['streaming_movies'] = df['streaming_movies'].replace(['No internet service', 'No', 'Yes'], [0,0,1])
    df['paperless_billing'] = df['paperless_billing'].replace(['No', 'Yes'], [0,1])
    df['churn'] = df['churn'].replace(['No', 'Yes'], [0,1])

    # Fixing total_charges by 1.) getting rid of rows where total_charges are null. 2.) Changing dtype to floats
    df_clean = df[~df['total_charges'].str.contains(" ")]
    df_clean.total_charges.astype(float)

    df_clean.rename(columns = {'gender' : 'is_male', 'partner' : 'has_partner', 'dependents': 'has_dependents',
     'phone_service': 'has_phone', 'multiple_lines': 'has_multi_line', 'online_security': 'has_onl_sec', 'online_backup': 'has_backup',
      'device_protection': 'has_dev_pro', 'tech_support': 'has_tech_supp', 'streaming_tv' : 'has_tv_strm',
       'streaming_movies': 'has_mv_strm', 'paperless_billing': 'has_pprless_bill', 'churn': 'has_churned'}, inplace = True)

    # split data into train, validate, test dfs
    train, validate, test = telco_split(df_clean)
    return train, validate, test

# Split newly cleaned data into train, validate, and test sets with churn being stratified
def telco_split(df):
    '''
    This function take in the telco data acquired by get_telco_data,
    performs a split and stratifies churn column.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.has_churned)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.has_churned)
    return train, validate, test