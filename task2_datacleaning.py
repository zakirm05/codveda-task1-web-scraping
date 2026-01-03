import pandas as pd

# 1. CSV file load karo
df = pd.read_csv("books_data.csv")

print("Original Data (first 5 rows):")
print(df.head())

# 2. Missing values check
print("\nMissing values count:")
print(df.isnull().sum())

# 3. Missing values remove (agar koi ho)
df.dropna(inplace=True)

# 4. Price column clean karo (£ / Â£ remove + number banana)
df["Price"] = df["Price"].str.replace("Â£", "", regex=False)
df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].astype(float)

# 5. Availability column clean karo (text → numeric)
df["Availability"] = df["Availability"].apply(
    lambda x: 1 if "In stock" in x else 0
)

# 6. Cleaned data save karo
df.to_csv("books_data_cleaned.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned Data (first 5 rows):")
print(df.head())
