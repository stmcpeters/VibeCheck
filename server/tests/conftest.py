import pytest
import psycopg2
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# fixture to set up and tear down the test database
@pytest.fixture
def db_connection():
  # connect to the test database
  connection = psycopg2.connect(
    host="localhost",
    database="test_vibecheck",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    port="5432"
  )

  # create cursor object to interact with the database
  cursor = connection.cursor()

  # set up users table
  cursor.execute('DROP TABLE IF EXISTS users CASCADE;')
  cursor.execute('''
                CREATE TABLE users (id SERIAL PRIMARY KEY,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                OAuth_id VARCHAR(255) DEFAULT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
                ''')
  
  # commit the changes
  connection.commit()

  # yield the connection object to the test function
  yield connection

  # roll back any failed transaction before teardown (to avoid leaving the database in an inconsistent state)
  if connection.status == psycopg2.extensions.STATUS_IN_TRANSACTION:
    connection.rollback()

  # tear down the test database
  cursor.execute('DROP TABLE IF EXISTS users CASCADE;')
  connection.commit()
  cursor.close()
  connection.close()