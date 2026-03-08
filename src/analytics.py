from data_processing import *

# Load data and print
df = load_data()

print(df.head())

print("\nTotal revenue:")
print(get_global_revenue(df))

print("\nRevenue by product:")
print(sales_by_product(df))

print("\nRevenue by region:")
print(sales_by_region(df))

print("\nRevenue by month:")
print(sales_by_month(df))
