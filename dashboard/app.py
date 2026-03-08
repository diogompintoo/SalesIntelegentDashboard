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

# Metrics
st.header("Global Revenue")
st.write(get_global_revenue(df))

# By product
st.header("Revenue by Product")
st.bar_chart(sales_by_product(df))

# By region
st.header("Revenue by region")
st.bar_chart(sales_by_region(df))

# By month
st.header("Revenue by month")
st.line_chart(sales_by_month(df))