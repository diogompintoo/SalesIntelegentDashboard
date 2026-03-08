import pandas as pd

#[L4 to L6] Load dataset
def load_data():
    df = pd.read_csv("../data/sales_data.csv")
    return df

#[L9 and L10] Calculate total revenue
def get_global_revenue (df):
    return df["revenue"].sum()

#[L13 and L14] Revenue by product
def sales_by_product (df):
    return df.groupby("product")["revenue"].sum()

#[L17 and L18]
def sales_by_region (df):
    return df.groupby("region")["revenue"].sum()

#[L20 to L25] Revenue by month
def sales_by_month(df):

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["revenue"].sum()

