import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",  # Replace with your host address
    port="5432",  # Replace with your port number
    user="ahanafshahriar",  # Replace with your username
    database="holdingData"  # Replace with your database name
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a SELECT query to retrieve all records from the table
cursor.execute("SELECT * FROM holdingData")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
