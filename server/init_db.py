import os
import psycopg2
# loads environment variables from a .env file
from dotenv import load_dotenv
# import requests module for HTTP requests
import requests
# import beautifulsoup for web scraping
from bs4 import BeautifulSoup
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
                    'category TEXT NOT NULL,'
                    'link VARCHAR(255) NOT NULL,'
                    'author VARCHAR(255) NOT NULL);'
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
    cursor.execute('INSERT INTO mood_logs (user_id, emoji_id, journal_entry, sentiment_score)'
                    'VALUES (%s, %s, %s, %s)',
                    (1, 1, 'today was a good day! i had a lot of fun building this app!', 0.8))
    print('Data inserted into mood logs successfully.')

    try:
        url = 'https://www.verywellmind.com/self-improvement-4157212'
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            soup = BeautifulSoup(response.content, 'html.parser')
            # print(soup.prettify())

            # find all elements needed
            titles = soup.find_all('span', class_='card__title-text')
            # for title in titles:
            #     print(title.text)
            links = soup.find_all('a', class_="comp mntl-card-list-items mntl-document-card mntl-card card card--no-image")
            # for link in links:
                # href = link.get('href')
                # print(href)
            categories = soup.find_all('div', class_='card__content')
            # for category in categories:
            #     category_title = category.get('data-tag')
            #     print(category_title)
            authors = soup.find_all('div', class_='card__byline mntl-card__byline')
            # for author in authors:
            #     print(author.get('data-byline'))
        else:
            print('Error:', response.status_code, response.text)
    except requests.exceptions.RequestException as e:
      print(f'Error fetching data from {url}: {e}')

    # insert data into the articles table
    print('Inserting data into the articles table...')
    # iterate through data and insert into articles table
    # zip() inserts all data in one command (best practice for matching data)
    for title, category, link, author in zip(titles, categories, links, authors):
      cursor.execute('''INSERT INTO articles (title, category, link, author) VALUES (%s, %s, %s, %s)''', (title.text.strip(), category.text.strip(), link['href'], author['data-byline']))

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
