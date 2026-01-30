import pandas as pd

# Load the CSV file
file_path = "Assignment python.csv"
df = pd.read_csv(file_path)

# Calculate price per square foot
df['price_per_sqft'] = df['price'] / df['sq__ft']

# Compute the average price per square foot
avg_price_per_sqft = df['price_per_sqft'].mean()

# Filter properties below average price per square foot
below_avg_df = df[df['price_per_sqft'] < avg_price_per_sqft]

# Save the filtered data to a new CSV
below_avg_df.to_csv("output.csv", index=False)

print(f"Filtered {len(below_avg_df)} properties below average price/foot ({avg_price_per_sqft:.2f}).")
