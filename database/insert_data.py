import psycopg2
import csv

# Connect to the database
conn = psycopg2.connect(
    dbname="covid19",
    user="postgres",
    password="SupersaiyaN117",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Open the processed CSV file
with open("processed_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    # Insert each row into the database
    for row in reader:
        cur.execute("""
            INSERT INTO covid19_data (province, country, date, cases)
            VALUES (%s, %s, %s, %s)
        """, row)

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()
print("Data inserted successfully into the database.")
