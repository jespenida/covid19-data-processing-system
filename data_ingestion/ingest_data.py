import psycopg2
import pandas as pd

# Load the processed data
data = pd.read_csv("processed_data.csv")

# Filter data for the U.S. only
data = data[data["Country"] == "US"]

# Connect to the database
conn = psycopg2.connect(
    dbname="covid19",
    user="postgres",
    password="SupersaiyaN117",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert data into the table
for index, row in data.iterrows():
    query = """
    INSERT INTO covid19_data (province, country, date, cases, deaths)
    VALUES (%s, %s, %s, %s, %s);
    """
    cur.execute(query, (row["Province"], row["Country"], row["Date"], row["Cases"], row["Deaths"]))

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
print("US data inserted successfully!")
