import pandas as pd


class DataFrame:
    df = pd.read_csv('C:/Users/João/Desktop/dataCRM/test.csv')
    identifier = df['identificador'].astype('int'),
    age = df['idade'].astype('int'),
    revenue = df['receita'].astype('float'),
    date = pd.to_datetime(df['data']),
    rate = df['nota'].astype('int'),
    dfYear = pd.to_datetime(df['data']).dt.year
    dfMonth = pd.to_datetime(df['data']).dt.month
    dfDay = pd.to_datetime(df['data']).dt.day
