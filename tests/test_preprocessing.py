import pandas as pd

from src.data_preprocessing import (
    clean_data
)


def test_datetime_conversion():

    df = pd.DataFrame({
        "signup_time": [
            "2024-01-01"
        ],
        "purchase_time": [
            "2024-01-02"
        ]
    })

    result = clean_data(df)

    assert str(
        result["signup_time"].dtype
    ).startswith(
        "datetime64"
    )
    