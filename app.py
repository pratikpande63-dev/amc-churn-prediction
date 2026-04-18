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

conn.close()