import pandas as pd

df = pd.read_csv("data/churn.csv")

print(df.shape)
print(df.head())
print(df.info())

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print(df['TotalCharges'].isnull().sum())

# customerID doesn't help prediction, drop it
df = df.drop('customerID', axis=1)

# fill the 11 missing TotalCharges with the median value
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

print(df.isnull().sum().sum())  # should print 0 now

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

print(df.dtypes)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model1 = LogisticRegression(max_iter=1000)
model1.fit(X_train, y_train)

pred1 = model1.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, pred1))
print(classification_report(y_test, pred1))

from sklearn.ensemble import RandomForestClassifier

model2 = RandomForestClassifier(random_state=42)
model2.fit(X_train, y_train)

pred2 = model2.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, pred2))
print(classification_report(y_test, pred2))

results = X_test.copy()
results['Actual_Churn'] = y_test
results['Predicted_Churn'] = pred1

results.to_csv('predictions.csv', index=False)
print("Predictions saved to predictions.csv")