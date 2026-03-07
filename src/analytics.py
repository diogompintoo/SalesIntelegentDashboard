import pandas as pd

# [L4] Upload sales file [L5] Show the starting lines of sales
df = pd.read_csv("../data/sales_data.csv")
print(df.head())

#[L8] Calculate all the revenue [L9] Print the value
total_revenue = df["revenue"].sum()
print("Total Revenue:", total_revenue)

#[L12 to L15] Group the sales by product and print
sales_by_product = df.groupby("product")["revenue"].sum

print("\nRevenue by product:")
print(sales_by_product)

#[L18 to L21] Group the sales by region and print
sales_by_region =df.groupby("region")["revenue"].sum

print("\nRevenue by region:")
print(sales_by_region)

#[L24] Convert in real date
df["date"] = pd.to_datetime(df["date"])

#[L27] Create a colum of month
df["month"] = df["date"].dt.to_period("M")

#[L30] Group all month sales and sum and print
sales_by_month = df.groupby("month")["revenue"].sum

print("\nRevenue by month:")
print(sales_by_month)






