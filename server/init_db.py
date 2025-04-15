import os
import psycopg2
# loads environment variables from a .env file
from dotenv import load_dotenv

# loads environment variables from .env file
load_dotenv()

# initializes the connection variable
connection = None

try:
  print("Connecting to the database...")
  # creates a connection to the PostgreSQL database
  connection = psycopg2.connect(
      host="localhost",
      database="vibe_check",
      user=os.environ['DB_USERNAME'],
      password=os.environ['DB_PASSWORD'],
      port="5432")
  print("Connected to the database.")

  # creates a cursor object to interact with the database
  cursor = connection.cursor()

  # execute SQL commands
  try:
    print("Creating the users table...")
    # drops the users table if it exists
    cursor.execute('DROP TABLE IF EXISTS users CASCADE;')
    cursor.execute('CREATE TABLE users (id SERIAL PRIMARY KEY,'
                    'email VARCHAR(255) NOT NULL,' 
                    'password VARCHAR(255) NOT NULL,'
                    'OAuth_id VARCHAR(255) DEFAULT NULL,'
                    'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'
                    )
    print("Users table created successfully.")

    print('Creating mood logs table...')
    # drops the mood logs table if it exists
    cursor.execute('DROP TABLE IF EXISTS mood_logs;')
    cursor.execute('CREATE TABLE mood_logs (id SERIAL PRIMARY KEY,'
                    'user_id INTEGER REFERENCES users(id),'
                    'emoji VARCHAR(255) NOT NULL,'
                    'journal_entry TEXT DEFAULT NULL,'
                    'sentiment_score FLOAT DEFAULT NULL,'
                    'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'
                  )
    print("Mood logs table created successfully.")

    # insert data into the users table
    print("Inserting data into the users table...")
    cursor.execute("INSERT INTO users (email, password)"
                    "VALUES (%s, %s)",
                    ('test@test.com',
                    'password123'))
    print("Data inserted into users table successfully.")

    # insert data into the mood logs table
    print('Inserting data into the mood logs table...')
    cursor.execute('INSERT INTO mood_logs (user_id, emoji, journal_entry, sentiment_score)'
                    'VALUES (%s, %s, %s, %s)',
                    (1, ':smile:', 'today was a good day! i had a lot of fun building this app!', 0.8))
    print('Data inserted into mood logs successfully.')

    # commits the changes to the database
    connection.commit()
    print("Changes committed to the vibe_check database.")

  except Exception as e:
      print(f"Error executing SQL commands: {e}")
      # rolls back the interaction in case of an error
      connection.rollback()

  finally:
    #  closes the cursor
    cursor.close()

except Exception as e:
  print(f"Error connecting to the database: {e}")

finally:
# closes the connection if it was created
  if connection:
    connection.close()
    print("Database connection closed.")
