import os
import psycopg2
# loads environment variables from a .env file
from dotenv import load_dotenv

# loads environment variables from .env file
load_dotenv()

# creates a connection to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="vibe_check",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    port="5432")

# creates a cursor object to interact with the database
cursor = connection.cursor()

# drops the users table if it exists
cursor.execute('DROP TABLE IF EXISTS users;')
cursor.execute('CREATE TABLE users (id SERIAL PRIMARY KEY,'
                'email VARCHAR(255) NOT NULL,' 
                'password VARCHAR(255) NOT NULL,'
                'OAuth_id VARCHAR(255),'
                'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'
                )

# insert data into the users table
cursor.execute("INSERT INTO users (email, password)"
                "VALUES (%s, %s)",
                ('test@test.com',
                'password123'))

# commits the changes to the database
connection.commit()

# closes the cursor and connection
cursor.close()
connection.close()
