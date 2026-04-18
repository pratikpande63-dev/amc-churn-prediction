import sqlite3
import pandas as pd

# Connect DB
conn = sqlite3.connect("amc_churn.db")

# Read CSV files
customers = pd.read_csv("data/customers.csv")
contracts = pd.read_csv("data/amc_contracts.csv")
service = pd.read_csv("data/service_history.csv")
interaction = pd.read_csv("data/interaction_history.csv")

# Insert into tables
customers.to_sql("customer", conn, if_exists="append", index=False)
contracts.to_sql("amc_contract", conn, if_exists="append", index=False)
service.to_sql("service_history", conn, if_exists="append", index=False)
interaction.to_sql("interaction_history", conn, if_exists="append", index=False)

# Save & close
conn.commit()
conn.close()

print("✅ Data inserted successfully!")