import pandas as pd

from src.data_preprocessing import (
    clean_data
)

from src.feature_engineering import (
    create_time_features,
    create_transaction_features
)

fraud = pd.read_csv(
    "../data/raw/Fraud_Data.csv"
)

fraud = clean_data(fraud)

fraud = create_time_features(
    fraud
)

fraud = create_transaction_features(
    fraud
)

fraud.to_csv(
    "../data/processed/fraud_processed.csv",
    index=False
)

print(
    "Features generated successfully"
)
