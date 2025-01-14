import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname="covid19",
    user="postgres",
    password="SupersaiyaN117",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Query: Daily cases for 'US'
query = """
SELECT date, SUM(cases) AS total_cases
FROM covid19_data
WHERE country = 'US'
GROUP BY date
ORDER BY date;
"""
cur.execute(query)

# Fetch and print results
results = cur.fetchall()
if results:
    print("Daily cases in US:")
    for row in results:
        print(f"Date: {row[0]}, Total Cases: {row[1]}")
else:
    print("No data found for the specified country (US).")

cur.close()
conn.close()
