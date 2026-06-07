import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from src.model_training import (
    train_logistic_regression
)

df = pd.read_csv(
    "../data/processed/fraud_processed.csv"
)

df = pd.get_dummies(
    df,
    drop_first=True
)

X = df.drop(
    "class",
    axis=1
)

y = df["class"]

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)

model = train_logistic_regression(
    X_train,
    y_train
)

print(
    "Model trained successfully"
)
