# ==========================================
# 📊 SALES DATA ANALYSIS PROJECT
# ==========================================

#  1: Setup & Load Data
# ------------------------------------------

# Import pandas library
import pandas as pd

# Load the CSV file
# (Update path if needed)
file_path = "sales_data.csv"
df = pd.read_csv(file_path)

print("✅ Data Loaded Successfully!\n")
#  2: Explore Data
# ------------------------------------------

print("📌 First 5 Rows:")
print(df.head(), "\n")
print("📌 Dataset Shape (Rows, Columns):")
print(df.shape, "\n")
print("📌 Column Names:")
print(df.columns, "\n")
print("📌 Data Types:")
print(df.dtypes, "\n")
print("📌 Missing Values:")
print(df.isnull().sum(), "\n")
#  3: Clean Data
# ------------------------------------------

# Remove duplicate rows
df = df.drop_duplicates()
# Handle missing values:
# Fill numeric columns with 0
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = df[numeric_cols].fillna(0)
# Fill categorical columns with "Unknown"
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna("Unknown")
print("✅ Data Cleaning Completed!\n")
#  4: Analyze Sales
# ------------------------------------------

# Make sure required columns exist:
# Assuming columns like: Product, Quantity, Price

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]
# Metric 1: Total Sales Revenue
total_revenue = df["Revenue"].sum()

# Metric 2: Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Metric 3: Best-Selling Product (by Revenue)
best_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

top_product_name = best_product.index[0]
top_product_revenue = best_product.iloc[0]

# Additional Metric: Average Order Value
average_revenue = df["Revenue"].mean()
#  5: Create Clean Formatted Report
# ------------------------------------------

print("=" * 50)
print("📊 SALES ANALYSIS REPORT")
print("=" * 50)
print(f"🧾 Total Revenue Generated : ₹{total_revenue:,.2f}")
print(f"📦 Total Quantity Sold     : {total_quantity}")
print(f"⭐ Best-Selling Product     : {top_product_name}")
print(f"💰 Revenue from Best Product: ₹{top_product_revenue:,.2f}")
print(f"📈 Average Revenue per Sale : ₹{average_revenue:,.2f}")

print("=" * 50)
# Optional: Show top 5 products
print("\n🏆 Top 5 Products by Revenue:")
print(best_product.head())