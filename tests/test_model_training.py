from sklearn.datasets import (
    make_classification
)

from src.model_training import (
    train_logistic_regression
)


def test_model_creation():

    X, y = make_classification(
        n_samples=100,
        n_features=5,
        random_state=42
    )

    model = train_logistic_regression(
        X,
        y
    )

    assert model is not None
    