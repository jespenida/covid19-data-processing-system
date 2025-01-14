import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = psycopg2.connect(
    dbname="covid19",
    user="postgres",
    password="SupersaiyaN117",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Query: Daily cases for US
query = """
SELECT date, SUM(cases) AS total_cases
FROM covid19_data
WHERE country = 'US'
GROUP BY date
ORDER BY date;
"""
cur.execute(query)

# Fetch data and load into a DataFrame
rows = cur.fetchall()
df = pd.DataFrame(rows, columns=["date", "total_cases"])
df["date"] = pd.to_datetime(df["date"])  # Convert dates to datetime

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["total_cases"], marker="o", linestyle="-", label="Total Cases")
plt.title("Daily COVID-19 Cases in the US", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Cases", fontsize=12)
plt.grid(True)
plt.legend()

# Save the plot as a JPG file
plt.savefig("daily_cases_us.jpg", format="jpg", dpi=300)
print("Plot saved as 'daily_cases_us.jpg'.")

plt.show()

# Close the connection
cur.close()
conn.close()
