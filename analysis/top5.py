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

# Query: Top 5 countries with the most entries
query = """
SELECT country, COUNT(*) AS entry_count
FROM covid19_data
GROUP BY country
ORDER BY entry_count DESC
LIMIT 5;
"""
cur.execute(query)

# Fetch and print results
results = cur.fetchall()
print("Top 5 countries with the most entries:")
for row in results:
    print(f"Country: {row[0]}, Entries: {row[1]}")

cur.close()
conn.close()
