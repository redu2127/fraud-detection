import pandas as pd


def load_fraud_data(path):
    return pd.read_csv(path)


def clean_data(df):

    df = df.copy()

    df = df.drop_duplicates()

    df["signup_time"] = pd.to_datetime(
        df["signup_time"]
    )

    df["purchase_time"] = pd.to_datetime(
        df["purchase_time"]
    )

    return df
