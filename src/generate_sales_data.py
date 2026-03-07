
import pandas as pd
import random
from datetime import datetime, timedelta

#[L7/L8] List of products and cat in same order, [L9] Regions of sales
products = ["Laptop", "Phone","Tablet","Headphones","Monitor"]
categories = ["Eletronics","Eletronics","Eletronics","Acessorioes","Eletronics"]
regions = ["Europe","North America","Asia","South America"]

#[L12] Starting date to generate sales, [L13]List to save sales data
start_date = datetime(2023, 1, 1)
data = []

#[L16 to L25] Loop to generate 5000 sales with random product, region quantity and price
for i in range(5000):
    date = start_date + timedelta(days=random.randint(0, 730))
    product_index = random.randint(0, len(products)-1)

    product = products[product_index]
    category = categories[product_index]

    region = random.choice(regions)
    quantity = random.randint(1, 5)
    price = random.randint(50,1100)

    revenue = quantity * price

#[L30 to L37] Save the sales data in a list
    data.append([
        date,
        product,
        category,
        region,
        quantity,
        revenue
        ])

#[L40 to L47] Convert the previous list in a table
df = pd.DataFrame(data, columns=[
    "date",
    "product",
    "category",
    "region",
    "quantity",
    "revenue"
])

#[L50] Save the data in a file
df.to_csv("../data/sales_data.csv", index=False)

print("Dataset created!")

