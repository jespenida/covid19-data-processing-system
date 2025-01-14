import psycopg2
import pandas as pd

# Connect to the database
conn = psycopg2.connect(
    dbname="covid19",
    user="postgres",
    password="SupersaiyaN117",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Query: Retrieve data for specific countries
query = """
SELECT country, date, SUM(cases) AS total_cases
FROM covid19_data
WHERE country IN ('US', 'India', 'Brazil', 'Russia', 'UK', 'France', 'Germany', 'Italy', 'Canada', 'China')
GROUP BY country, date
ORDER BY date, country;
"""
cur.execute(query)

# Fetch results and load into a DataFrame
rows = cur.fetchall()
df = pd.DataFrame(rows, columns=["Country", "Date", "Total_Cases"])

# Pivot the data to create a table where each country is a column
pivot_df = df.pivot(index="Date", columns="Country", values="Total_Cases")

# Ensure data is numeric
pivot_df = pivot_df.fillna(0)  # Replace missing values with 0

# Calculate correlations between countries
correlation_matrix = pivot_df.corr()

# Save the correlation matrix to a CSV file
correlation_matrix.to_csv("focused_correlation_matrix.csv")
print("Correlation matrix saved to 'focused_correlation_matrix.csv'.")

# Close the connection
cur.close()
conn.close()
