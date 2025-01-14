import pandas as pd

# Step 1: Load the raw dataset
data = pd.read_csv("covid19_data.csv")

# Step 2: Drop unnecessary columns (Lat, Long)
if "Lat" in data.columns and "Long" in data.columns:
    data = data.drop(["Lat", "Long"], axis=1)

# Step 3: Add a placeholder 'Deaths' column
if "Deaths" not in data.columns:
    print("Warning: 'Deaths' column is missing. Adding a placeholder column.")
    data["Deaths"] = None

# Step 4: Reshape the data for easier database storage
data = data.melt(
    id_vars=["Province/State", "Country/Region", "Deaths"],
    var_name="Date",
    value_name="Cases"
)

# Step 5: Rename columns for consistency
data.columns = ["Province", "Country", "Deaths", "Date", "Cases"]

# Step 6: Save the cleaned data
data.to_csv("processed_data.csv", index=False)
print("Data has been processed and saved as 'processed_data.csv'.")
print("Preview of the processed data:")
print(data.head())
