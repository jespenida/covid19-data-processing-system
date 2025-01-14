import psycopg2

# Step 1: Connect to the 'covid19' database
conn = psycopg2.connect(
    dbname="covid19",           # Connect to the database you created
    user="postgres",            # Replace with your username
    password="SupersaiyaN117",  # Replace with your password
    host="localhost",
    port="5432"
)

# Step 2: Create a cursor object
cur = conn.cursor()

# Step 3: Open the SQL schema file and execute its contents
with open("database/schema.sql", "r") as file:
    schema = file.read().strip()  # Remove leading/trailing whitespace

if schema:  # Only execute if the schema is not empty
    cur.execute(schema)
    print("Database table 'covid19_data' created successfully.")
else:
    print("Schema file is empty. No changes were made.")

# Step 4: Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()
