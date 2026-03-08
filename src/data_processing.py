import os
import pandas as pd

#[L5 to L9] Load dataset
def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data","sales_data.csv")
    df = pd.read_csv(file_path)
    return df

#[L11 and L13] Calculate total revenue
def get_global_revenue (df):
    return df["revenue"].sum()

#[L16 and L17] Revenue by product
def sales_by_product (df):
    return df.groupby("product")["revenue"].sum()

#[L20 and L21]
def sales_by_region (df):
    return df.groupby("region")["revenue"].sum()

#[L24 to L28] Revenue by month
def sales_by_month(df):

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["revenue"].sum()

