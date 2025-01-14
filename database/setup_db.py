import psycopg2

# Connect to the 'covid19' database
conn = psycopg2.connect(
    dbname="covid19",           
    user="postgres",           
    password="SupersaiyaN117",  
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

#  Open the SQL schema file and execute its contents
with open("database/schema.sql", "r") as file:
    schema = file.read().strip()  

if schema:  
    cur.execute(schema)
    print("Database table 'covid19_data' created successfully.")
else:
    print("Schema file is empty. No changes were made.")

# Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()
