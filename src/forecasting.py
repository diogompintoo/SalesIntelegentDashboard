import pandas as pd
from sklearn.linear_model import LinearRegression
from src.data_processing import load_data

df = load_data()

# Prepare data
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

# Group sales by month
monthly_sales = df.groupby("month")["revenue"].sum()

# Convert index in numbers
monthly_sales = monthly_sales.reset_index()
monthly_sales["month_num"] = range(len(monthly_sales))

# Define data model
X = monthly_sales[["month_num"]]
y = monthly_sales["revenue"]

# Create model
model = LinearRegression()
model.fit(X,y)

# Predict next month
next_month = pd.DataFrame({"month_num":[len(monthly_sales)]})
prediction = model.predict(next_month)

print("Predicted revenue next month:")
print(prediction[0])

