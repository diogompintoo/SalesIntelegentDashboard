import streamlit as st
import sys
import os

# allow imports from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_processing import (
    load_data,
    get_global_revenue,
    sales_by_product,
    sales_by_region,
    sales_by_month
)

# Page title
st.title("Sales Intelligent Dashboard")

# Load data
df = load_data()

# KPI
st.metric("Total Revenue", get_global_revenue(df))

# Filter
region =st.selectbox("Select Region", df["region"].unique())

# Filter dataset
df_filtered = df[df["region"]== region]


                    # Charts
# By product
st.header("Revenue by Product")
st.bar_chart(sales_by_product(df_filtered))

# By region
st.header("Revenue by region")
st.bar_chart(sales_by_region(df_filtered))

# By month
st.header("Revenue by month")
st.line_chart(sales_by_month(df_filtered))
