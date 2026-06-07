# Fraud Detection for E-commerce and Bank Transactions

## Overview

This project develops machine learning models to detect fraudulent transactions in e-commerce and banking datasets.

The objective is to identify fraud effectively while minimizing false positives through data preprocessing, feature engineering, machine learning, and model explainability.

---

## Datasets

### Fraud_Data.csv
E-commerce transaction dataset.

### creditcard.csv
Credit card transaction dataset.

### IpAddress_to_Country.csv
IP address range mapping dataset used to enrich transaction data with country information.

---

## Project Structure

fraud-detection/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── eda-fraud-data.ipynb
│   ├── eda-creditcard.ipynb
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   └── shap-explainability.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── evaluation.py
│
├── scripts/
│   ├── generate_features.py
│   └── train_model.py
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_feature_engineering.py
│   └── test_model_training.py
│
├── requirements.txt
├── README.md
└── .gitignore
---

## Task 1: Data Analysis and Preprocessing

### Data Cleaning

- Duplicate removal
- Datetime conversion
- Data validation

### Exploratory Data Analysis

- Fraud distribution analysis
- Numerical feature analysis
- Categorical feature analysis
- Correlation analysis

### Feature Engineering

Created features:

- time_since_signup_hours
- hour_of_day
- day_of_week
- user_transaction_count
- device_transaction_count

### Geolocation Enrichment

- IP address processing
- Country mapping

### Class Imbalance Handling

- SMOTE Oversampling

---

## Task 2: Model Building

Models trained:

1. Logistic Regression
2. Random Forest

Evaluation Metrics:

- Precision
- Recall
- F1 Score
- AUC-PR
- Confusion Matrix

---

## Task 3: Explainability

Feature importance analysis was used to identify the most influential predictors.

Top features included:

- time_since_signup_hours
- device_transaction_count
- ip_address
- purchase_value
- age

---

## Results

### Logistic Regression

F1 Score: 0.619

AUC-PR: 0.727

## Business Recommendations

1. Monitor transactions occurring shortly after account creation.
2. Investigate repeated device usage patterns.
3. Implement additional verification for high-risk transactions.
4. Use transaction timing as an early fraud indicator.


