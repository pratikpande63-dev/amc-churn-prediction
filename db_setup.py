<<<<<<< HEAD
import sqlite3

# Create database
conn = sqlite3.connect("amc_churn.db")
cursor = conn.cursor()

# Customer Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    industry TEXT,
    city TEXT,
    created_at DATE
)
""")

# AMC Contract Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS amc_contract (
    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    start_date DATE,
    end_date DATE,
    contract_value REAL,
    status TEXT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

# Service History Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS service_history (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    service_date DATE,
    issue_type TEXT,
    resolution_time REAL,
    satisfaction_score INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

# Interaction History Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interaction_history (
    interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    interaction_type TEXT,
    date DATE,
    outcome TEXT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

# Prediction Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    churn_probability REAL,
    risk_category TEXT,
    prediction_date DATE,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

conn.commit()
conn.close()

=======
import sqlite3

# Create database
conn = sqlite3.connect("amc_churn.db")
cursor = conn.cursor()

# Customer Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    industry TEXT,
    city TEXT,
    created_at DATE
)
""")

# AMC Contract Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS amc_contract (
    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    start_date DATE,
    end_date DATE,
    contract_value REAL,
    status TEXT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

# Service History Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS service_history (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    service_date DATE,
    issue_type TEXT,
    resolution_time REAL,
    satisfaction_score INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

# Interaction History Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interaction_history (
    interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    interaction_type TEXT,
    date DATE,
    outcome TEXT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

# Prediction Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    churn_probability REAL,
    risk_category TEXT,
    prediction_date DATE,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)
""")

conn.commit()
conn.close()

>>>>>>> 16f00a1 (first commit)
print("✅ Database and tables created successfully!")