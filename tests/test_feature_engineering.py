import pandas as pd

from src.feature_engineering import (
    create_time_features
)


def test_time_since_signup():

    df = pd.DataFrame({
        "signup_time": [
            pd.Timestamp(
                "2024-01-01 10:00:00"
            )
        ],
        "purchase_time": [
            pd.Timestamp(
                "2024-01-01 12:00:00"
            )
        ]
    })

    result = create_time_features(
        df
    )

    assert (
        result[
            "time_since_signup_hours"
        ][0]
        == 2
    )
    