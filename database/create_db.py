import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",          
    user="postgres",           
    password="SupersaiyaN117", 
    host="localhost",
    port="5432"
)

# Allow creating databases
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor object
cur = conn.cursor()

# SQL to create a new database
cur.execute("CREATE DATABASE covid19;")

# Close the connection
cur.close()
conn.close()
print("Database 'covid19' created successfully.")
