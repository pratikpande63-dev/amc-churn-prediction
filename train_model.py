<<<<<<< HEAD
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Connect to DB
conn = sqlite3.connect("amc_churn.db")

# Load data
customers = pd.read_sql("SELECT * FROM customer", conn)
contracts = pd.read_sql("SELECT * FROM amc_contract", conn)
service = pd.read_sql("SELECT * FROM service_history", conn)

# Merge data
df = customers.merge(contracts, on="customer_id")
df = df.merge(service, on="customer_id")

# Feature Engineering
df['avg_resolution_time'] = df.groupby('customer_id')['resolution_time'].transform('mean')
df['avg_satisfaction'] = df.groupby('customer_id')['satisfaction_score'].transform('mean')

# Define churn (target variable)
df['churn'] = df['status'].apply(lambda x: 1 if x == 'Expired' else 0)

# Features
X = df[['contract_value', 'avg_resolution_time', 'avg_satisfaction']]
y = df['churn']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
df['churn_probability'] = model.predict_proba(X)[:, 1]

# Add risk category
def categorize_risk(prob):
    if prob > 0.7:
        return "High"
    elif prob > 0.4:
        return "Medium"
    else:
        return "Low"

df['risk_category'] = df['churn_probability'].apply(categorize_risk)

# Prepare prediction data
prediction_df = df[['customer_id', 'churn_probability', 'risk_category']].drop_duplicates()
prediction_df['prediction_date'] = pd.Timestamp.today().date()

# Save to DB
prediction_df.to_sql("prediction", conn, if_exists="replace", index=False)

print("✅ Predictions saved to database!")
print(prediction_df)

conn.close()
=======
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Connect to DB
conn = sqlite3.connect("amc_churn.db")

# Load data
customers = pd.read_sql("SELECT * FROM customer", conn)
contracts = pd.read_sql("SELECT * FROM amc_contract", conn)
service = pd.read_sql("SELECT * FROM service_history", conn)

# Merge data
df = customers.merge(contracts, on="customer_id")
df = df.merge(service, on="customer_id")

# Feature Engineering
df['avg_resolution_time'] = df.groupby('customer_id')['resolution_time'].transform('mean')
df['avg_satisfaction'] = df.groupby('customer_id')['satisfaction_score'].transform('mean')

# Define churn (target variable)
df['churn'] = df['status'].apply(lambda x: 1 if x == 'Expired' else 0)

# Features
X = df[['contract_value', 'avg_resolution_time', 'avg_satisfaction']]
y = df['churn']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
df['churn_probability'] = model.predict_proba(X)[:, 1]

# Add risk category
def categorize_risk(prob):
    if prob > 0.7:
        return "High"
    elif prob > 0.4:
        return "Medium"
    else:
        return "Low"

df['risk_category'] = df['churn_probability'].apply(categorize_risk)

# Prepare prediction data
prediction_df = df[['customer_id', 'churn_probability', 'risk_category']].drop_duplicates()
prediction_df['prediction_date'] = pd.Timestamp.today().date()

# Save to DB
prediction_df.to_sql("prediction", conn, if_exists="replace", index=False)

print("✅ Predictions saved to database!")
print(prediction_df)

import joblib

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model saved!")

conn.close()
>>>>>>> 16f00a1 (first commit)
