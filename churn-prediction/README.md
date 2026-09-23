# Churn Prediction Model

## Objective

Predict which customers are likely to churn (leave the platform) using the Telco Customer Churn dataset.

## Dataset

- Source: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (Kaggle)
- 7,043 rows, 21 columns
- Target column: `Churn` (Yes/No)

## Preprocessing Steps

1. **Dropped `customerID`** — unique identifier, not useful for prediction.
2. **Fixed `TotalCharges`** — was stored as text due to blank values; converted to numeric with `pd.to_numeric(errors='coerce')`.
3. **Handled missing values** — 11 rows had missing `TotalCharges` after conversion; filled with the column median.
4. **Encoded categorical variables** — all text columns (e.g. `gender`, `Contract`, `PaymentMethod`, `Churn`) encoded to numeric using `LabelEncoder`.
5. **Train/test split** — 80% train, 20% test, `random_state=42` for reproducibility.

## Models Evaluated

| Model               | Accuracy | Precision (Churn) | Recall (Churn) | F1 (Churn) |
| ------------------- | -------- | ----------------- | -------------- | ---------- |
| Logistic Regression | 81.7%    | 0.68              | 0.58           | 0.63       |
| Random Forest       | 79.6%    | 0.66              | 0.47           | 0.55       |

## Model Selection

**Logistic Regression** was selected as the final model.

- Higher overall accuracy (81.7% vs 79.6%).
- Higher recall on the churn class (0.58 vs 0.47) — for churn prediction, failing to flag an at-risk customer (false negative) is more costly than a false alarm, so recall on the "Yes" class is the more important metric here.
- Random Forest was more conservative and missed more actual churners despite similar precision.

## Output

Predictions on the test set (actual vs predicted churn, plus all input features) are saved to `predictions.csv`.

## How to Run

```
pip install pandas scikit-learn
python churn_model.py
```
