from sklearn.metrics import (
    f1_score,
    average_precision_score
)


def evaluate_model(
    model,
    X_test,
    y_test
):

    predictions = model.predict(
        X_test
    )

    probabilities = (
        model.predict_proba(
            X_test
        )[:, 1]
    )

    return {
        "f1_score": f1_score(
            y_test,
            predictions
        ),
        "auc_pr": average_precision_score(
            y_test,
            probabilities
        )
    }
