import pandas as pd


def create_time_features(df):

    df = df.copy()

    df["time_since_signup_hours"] = (
        df["purchase_time"]
        - df["signup_time"]
    ).dt.total_seconds() / 3600

    df["hour_of_day"] = (
        df["purchase_time"]
        .dt.hour
    )

    df["day_of_week"] = (
        df["purchase_time"]
        .dt.dayofweek
    )

    return df


def create_transaction_features(df):

    df = df.copy()

    user_counts = (
        df["user_id"]
        .value_counts()
    )

    device_counts = (
        df["device_id"]
        .value_counts()
    )

    df["user_transaction_count"] = (
        df["user_id"]
        .map(user_counts)
    )

    df["device_transaction_count"] = (
        df["device_id"]
        .map(device_counts)
    )

    return df
