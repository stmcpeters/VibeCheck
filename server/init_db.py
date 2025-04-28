import os
import psycopg2
# loads environment variables from a .env file
from dotenv import load_dotenv

# loads environment variables from .env file
load_dotenv()

# initializes the connection variable
connection = None
# initializes the cursor variable
cursor = None

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

    print('Creating emojis table...')
    # drops the emojis table if it exists
    cursor.execute('DROP TABLE IF EXISTS emojis CASCADE;')
    cursor.execute('CREATE TABLE emojis (id SERIAL PRIMARY KEY,'
                    'emoji VARCHAR(255) NOT NULL,'
                    'label TEXT NOT NULL);'
                    )
    print("Emoji table created successfully.") 

    print('Creating mood logs table...')
    # drops the mood logs table if it exists
    cursor.execute('DROP TABLE IF EXISTS mood_logs;')
    cursor.execute('CREATE TABLE mood_logs (id SERIAL PRIMARY KEY,'
                    'user_id INTEGER REFERENCES users(id),'
                    'emoji_id INTEGER NOT NULL REFERENCES emojis(id),'
                    'journal_entry TEXT DEFAULT NULL,'
                    'sentiment_score FLOAT DEFAULT NULL,'
                    'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'
                  )
    print("Mood logs table created successfully.")

    print('Creating webscraped articles table...')
    # drops the articles table if it exists
    cursor.execute('DROP TABLE IF EXISTS articles;')
    cursor.execute('CREATE TABLE articles (id SERIAL PRIMARY KEY,'
                    'title VARCHAR(255) NOT NULL,'
                    'content TEXT NOT NULL,'
                    'url VARCHAR(255) NOT NULL,'
                    'read_time VARCHAR(255) NOT NULL);'
                    )
    print("Articles table created successfully.") 

    # insert data into the users table
    print("Inserting data into the users table...")
    cursor.execute("INSERT INTO users (email, password)"
                    "VALUES (%s, %s)",
                    ('test@test.com',
                    'password123'))
    print("Data inserted into users table successfully.")

    # insert data into the emojis table
    print("Inserting data into the emojis table...")
    emojis = [('😀', 'happy'),('😐', 'neutral'),('☹️', 'unhappy')]
    cursor.executemany("INSERT INTO emojis (emoji, label)"
                    "VALUES (%s, %s)",
                    emojis)
    print("Data inserted into emojis table successfully.")

    # insert data into the mood logs table
    print('Inserting data into the mood logs table...')
    values = [
    (1, 1, "Today was a great day! I felt really motivated and was able to finish a lot of tasks ahead of schedule. I also had a great brainstorming session with my team.", 0.9),
    (1, 3, "Feeling a bit stressed out today. I encountered a lot of unexpected bugs in my code, and it really drained my energy. Hoping tomorrow will be smoother.", 0.4),
    (1, 2, "Had a productive morning checking things off my to-do list, but by the afternoon, I started feeling a bit tired and distracted. Need to find better balance.", 0.6),
    (1, 1, "It was a pretty chill day overall. I managed to finish my assignments early and even squeezed in some time to read a few chapters of a book I just started.", 0.8),
    (1, 3, "Today was overwhelming from the start. My meetings ran longer than expected, and I felt like I didn’t have enough time to catch up on my personal projects.", 0.2),
    (1, 1, "Great energy all day today! I knocked out a bunch of work tasks, had some awesome conversations with friends, and even found time for a sunset walk.", 0.85),
    (1, 3, "Not the best day. I woke up feeling off and couldn’t really get into the groove of things. I kept second-guessing myself and getting frustrated easily.", 0.3),
    (1, 1, "Honestly, today was amazing. Everything just clicked — I felt super creative while coding, got positive feedback from my manager, and treated myself to a nice dinner.", 0.95),
    (1, 3, "Today felt like an uphill battle. Every small thing seemed harder than usual, and I’m feeling pretty drained. Hoping a good night’s sleep helps reset.", 0.1),
    (1, 2, "Had a decent day overall. Nothing too exciting happened, but I stayed consistent with my work and made some slow but steady progress on my goals.", 0.5)]
    cursor.executemany('INSERT INTO mood_logs (user_id, emoji_id, journal_entry, sentiment_score)'
                    'VALUES (%s, %s, %s, %s)',
                    values)
    print('Data inserted into mood logs successfully.')

    # insert data into the articles table
    print('Inserting data into the articles table...')
    cursor.execute('INSERT INTO articles (title, content, url, read_time)'
                    'VALUES (%s, %s, %s, %s)',
                    ('Test Article',
                    'This is only a test article. It is not real.',
                    'http://test.com/',
                    '12 min read'))

    # commits the changes to the database
    connection.commit()
    print("Changes committed to the vibe_check database.")

  # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
  except psycopg2.OperationalError as e:
    print(f'Operational error: {e}')
    # rolls back the interaction in case of an error
    connection.rollback()
  
  # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
  except psycopg2.ProgrammingError as e:
    print(f'Programming error: {e}')
    # rolls back the interaction in case of an error
    connection.rollback()

  # error handling for constraints violations
  except psycopg2.IntegrityError as e:
    print(f'Integrity error: {e}')
    # rolls back the interaction in case of an error
    connection.rollback()
  
  # error handling for any other possible errors
  except Exception as e:
    print(f"Error executing SQL commands: {e}")
    # rolls back the interaction in case of an error
    connection.rollback()

  finally:
    if cursor:
      #  closes the cursor
      cursor.close()

except Exception as e:
  print(f"Error connecting to the database: {e}")

finally:
# closes the connection if it was created
  if connection:
    connection.close()
    print("Database connection closed.")
