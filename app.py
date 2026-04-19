<<<<<<< HEAD
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
sqlite3.connect("amc_churn.db")


# Page Title
st.set_page_config(page_title="AMC Churn Dashboard", layout="wide")

st.title("📊 AMC Churn Prediction Dashboard")

# Connect DB
conn = sqlite3.connect("amc_churn.db")

# Load data
df = pd.read_sql("SELECT * FROM prediction", conn)

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("High Risk Customers", len(df[df['risk_category'] == 'High']))
col3.metric("Low Risk Customers", len(df[df['risk_category'] == 'Low']))

st.markdown("---")

# Table View
st.subheader("📋 Customer Risk Details")
st.dataframe(df)



st.subheader("📊 Risk Distribution (Visual)")

fig, ax = plt.subplots()
df['risk_category'].value_counts().plot(kind='bar', ax=ax)

st.pyplot(fig)

# Filter option
st.subheader("🔍 Filter by Risk Category")
risk_filter = st.selectbox("Select Risk Level", ["All", "High", "Medium", "Low"])

if risk_filter != "All":
    filtered_df = df[df['risk_category'] == risk_filter]
    st.dataframe(filtered_df)

    st.subheader("👤 Customer Details")

customer_id = st.selectbox("Select Customer ID", df['customer_id'].unique())

customer_data = df[df['customer_id'] == customer_id]

st.write(customer_data)

st.subheader("💡 Insights")

high_risk_count = len(df[df['risk_category'] == 'High'])

if high_risk_count > 0:
    st.warning(f"{high_risk_count} customers are at HIGH risk of churn. Immediate action required!")
else:
    st.success("All customers are in safe zone.")

    st.subheader("🎯 Recommended Actions")

def get_recommendation(risk):
    if risk == "High":
        return "Offer discount + assign senior support"
    elif risk == "Medium":
        return "Follow-up call + engagement"
    else:
        return "Send renewal reminder"

df['recommendation'] = df['risk_category'].apply(get_recommendation)

st.dataframe(df[['customer_id', 'risk_category', 'recommendation']])

=======
# ================================
# 🔐 LOGIN SYSTEM
# ================================
import streamlit as st
import joblib
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Load ML model
model = joblib.load("model.pkl")
"""
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid credentials")

# Session control
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

# Logout
if st.sidebar.button("🚪 Logout"):
    st.session_state["logged_in"] = False
    st.rerun()

"""
# ================================
# ⚙️ APP CONFIG
# ================================
st.set_page_config(page_title="AMC Churn AI", layout="wide")

menu = st.sidebar.radio("📌 Navigation", ["Dashboard", "Customers", "Insights"])


# ================================
# 🗄️ DATABASE CONNECTION
# ================================
conn = sqlite3.connect("amc_churn.db")

df = pd.read_sql("""
SELECT c.customer_id, c.name, p.churn_probability, p.risk_category
FROM prediction p
JOIN customer c ON p.customer_id = c.customer_id
""", conn)


# ================================
# 📊 DASHBOARD
# ================================
if menu == "Dashboard":

    st.title("📊 AMC Churn Dashboard")

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", len(df))
    col2.metric("High Risk", len(df[df['risk_category'] == 'High']))
    col3.metric("Low Risk", len(df[df['risk_category'] == 'Low']))

    st.markdown("---")

    # Table
    st.subheader("📋 Customer Data")
    st.dataframe(df.sort_values(by="churn_probability", ascending=False))

    # Chart
    st.subheader("📊 Risk Distribution")
    fig, ax = plt.subplots()
    df['risk_category'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

    # ================================
    # 🤖 REAL-TIME ML PREDICTION
    # ================================
    st.subheader("🤖 Real-Time Churn Prediction")

    contract_value = st.number_input("Contract Value", value=50000)
    resolution_time = st.number_input("Avg Resolution Time", value=5)
    satisfaction = st.slider("Satisfaction Score", 1, 5, 3)

    if st.button("Predict Churn"):

        input_data = [[contract_value, resolution_time, satisfaction]]
        prob = model.predict_proba(input_data)[0][1]

        # Risk logic
        if prob > 0.7:
            risk = "High"
        elif prob > 0.4:
            risk = "Medium"
        else:
            risk = "Low"

        st.success(f"Churn Probability: {round(prob, 2)}")
        st.warning(f"Risk Category: {risk}")

        # Recommendation
        if risk == "High":
            st.error("👉 Action: Offer discount + assign senior support")
        elif risk == "Medium":
            st.info("👉 Action: Follow-up call")
        else:
            st.success("👉 Action: Send renewal reminder")


# ================================
# 👤 CUSTOMER SECTION
# ================================
elif menu == "Customers":

    st.title("👤 Customer Details")

    # Select customer
    customer_name = st.selectbox("Select Customer", df['name'].unique())

    # Filter data
    customer_data = df[df['name'] == customer_name]

    # Display
    st.write(customer_data)

    st.dataframe(customer_data[['name', 'churn_probability', 'risk_category']])


# ================================
# 💡 INSIGHTS SECTION
# ================================
elif menu == "Insights":

    st.title("💡 Business Insights")

    high_risk_count = len(df[df['risk_category'] == 'High'])

    if high_risk_count > 0:
        st.warning(f"{high_risk_count} customers are at HIGH risk of churn!")
    else:
        st.success("All customers are safe.")

    # Recommendation logic
    def get_recommendation(risk):
        if risk == "High":
            return "Offer discount + assign senior support"
        elif risk == "Medium":
            return "Follow-up call + engagement"
        else:
            return "Send renewal reminder"

    df['recommendation'] = df['risk_category'].apply(get_recommendation)

    st.subheader("🎯 Recommendations")
    st.dataframe(df[['name', 'risk_category', 'recommendation']])

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", len(df))
    col2.metric("High Risk", len(df[df['risk_category']=="High"]))
    col3.metric("Medium Risk", len(df[df['risk_category']=="Medium"]))


# ================================
# 🔚 CLOSE DB
# ================================
>>>>>>> 16f00a1 (first commit)
conn.close()