from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from openai import OpenAI
import os
import psycopg2
import bcrypt
# import beautifulsoup for web scraping
from bs4 import BeautifulSoup
# import requests module for HTTP requests
import requests
# loads environment variables from a .env file
# imports and loads environment variables from a .env file
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API key
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

# creates Flask app instance
app = Flask(__name__)
# sets the secret key for session management
app.secret_key = os.environ.get('SECRET_KEY')
# get the environment (default to 'development')
ENV = os.getenv('FLASK_ENV', 'development')

# Dynamically set allowed origins based on environment
allowed_origins = [
    "http://localhost:5173",  # Frontend development URL
    "https://vibe-check-final.netlify.app"  # Frontend production URL
]

# Configure CORS
CORS(app, resources={r"/*": {"origins": allowed_origins}}, supports_credentials=True)

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin')
    if origin in allowed_origins:
        response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# sets the session cookie name
app.config['SESSION_COOKIE_SAME_SITE'] = 'None'
# true if using HTTPS for production
# false if using HTTP for development
app.config['SESSION_COOKIE_SECURE'] = True if ENV == 'production' else False
# sets the session type to filesystem
app.config['SESSION_TYPE'] = 'filesystem'
# initializes the session
Session(app)


# creates a connection to the PostgreSQL database
# using environment variables for credentials
def get_db_connection():
    try:
        # loads environment variables from .env file
        load_dotenv()
        connection = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            database=os.environ.get('DB_NAME', 'vibe_check'),
            user=os.environ.get('DB_USERNAME', 'postgres'),
            password=os.environ.get('DB_PASSWORD', ''),
            port=os.environ.get('DB_PORT', '5432')
        )
        return connection
    # error handling for connection failure, invalid DB credentials, etc
    except psycopg2.OperationalError as e:
        print(f'Database connection error: {e}')
        raise
    # will catch any other errors
    except Exception as e:
        print(f'Error connecting to the database: {e}')
        raise

####################### USERS #################################

# fetches all users from users table
@app.route('/users', methods=['GET'])
def get_users():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users;')
        users = cursor.fetchall()
        # will return users data and a 200 status code (successful)
        return jsonify({'users': users}), 200
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch users'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error fetching users from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# creates a new user 
@app.route('/register', methods=['POST'])
def add_user():
    connection = None
    cursor = None

    try:
        if request.method == 'POST':

            # parse the JSON data
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            
            # validate input
            if not email or not password:
                return jsonify({"error": "Missing required fields"}), 400
            
            # connect to database
            connection = get_db_connection()
            cursor = connection.cursor()

            # check if email already exists
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            if cursor.fetchone():
                return jsonify({'error': 'Email already exists'}), 400

            # converting password to an array of bytes
            password_bytes = password.encode('utf-8');
            # hashing the password and generating a salt
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            # converting the hashed password to a string
            stored_password = str(hashed_password.decode('utf-8'))
            # print('hashed password: ', hash)
            # print('stored password: ', stored_password)

            # query to insert new user
            cursor.execute('''INSERT INTO users (email, password) VALUES (%s , %s)''', (email, stored_password))
            # commit changes
            connection.commit()
            return jsonify({'message': 'new user has been created!'}), 200
        
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to create new user'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error adding user to the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# login a user
@app.route('/login', methods=['POST'])
def login_user():
    connection = None
    cursor = None
    try:
        # gets the data from the request
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400
        
        # connect to database
        connection = get_db_connection()
        cursor = connection.cursor()
        # query to select user by email
        cursor.execute('''SELECT * FROM users WHERE email = %s''', (email,))
        user = cursor.fetchone()

        # check if user exists
        if user is None:
            return jsonify({'message': 'Invalid email or password'}), 404
        
        # convert password to bytes
        password = password.encode('utf-8')
        # get the hashed password from the database
        stored_password = user[2].encode('utf-8')

        # check if password matches
        if user and bcrypt.checkpw(password, stored_password):
            session['user_id'] = user[0]
            print(f"Session set: {session['user_id']}")
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'message': 'Invalid email or password'}), 401


    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to authenticate user'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error during login: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# gets the current logged in user
@app.route('/current_user', methods=['GET'])
def get_current_user():
    connection = None
    cursor = None

    try:
        user_id = session.get('user_id')
        print(f'Session user_id: {user_id}')
        if user_id is None:
            return jsonify({'error': 'User not logged in'}), 401
        
        # connect to database
        connection = get_db_connection()
        cursor = connection.cursor()
        # query to select user by id
        cursor.execute('''SELECT * FROM users WHERE id = %s''', (user_id,))
        user = cursor.fetchone()
        if user:
            return jsonify({'user': user}), 200
        
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch user'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error fetching user from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# log out a user
@app.route('/logout', methods=['POST'])
def logout_user():
    session.clear()
    return jsonify({'message': 'User logged out successfully!'}), 200

# fetches a user by ID
@app.route('/get_user/<int:id>', methods=['GET'])
def get_user(id):
    connection = None
    cursor = None

    try:
        if request.method == 'GET':

            # connect to database
            connection = get_db_connection()
            cursor = connection.cursor()
            # query to select user by id
            cursor.execute('''SELECT * FROM users WHERE id = %s''', (id,))
            user = cursor.fetchone()
            return jsonify({'user': user}), 200
        
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch user'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error fetching user from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# updates a user's info
@app.route('/update_user/<int:id>', methods=['PUT'])
def update_user(id):
    connection = None
    cursor = None

    try:
        if request.method == 'PUT':

            # parse the JSON data
            data = request.get_json()
            new_email = data.get('email')
            new_password = data.get('password')
            
            # validate input
            if not new_email or not new_password:
                return jsonify({"error": "Email and password are required"}), 400
            
            # connect to database
            connection = get_db_connection()
            cursor = connection.cursor()
            # query to update an existing user
            cursor.execute('''UPDATE users SET email = %s, password = %s WHERE id = %s''', (new_email, new_password, id))
            # commit changes
            connection.commit()
            return jsonify({'message': 'User has been updated!'}), 200
        
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to update user'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error updating user in the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# delete a user
@app.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    connection = None
    cursor = None

    try:
        if request.method == 'DELETE':

            # connect to database
            connection = get_db_connection()
            cursor = connection.cursor()
            # query to delete user
            cursor.execute('''DELETE FROM users WHERE id = %s''', (id,))
            # commit changes
            connection.commit()
            return jsonify({'message': 'User has been deleted!'}), 200
        
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to delete user'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error deleting user from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

##################### end of users ##################################

######################### EMOJIS ###################################

# fetches all emojis from emojis table
@app.route('/emojis', methods=['GET'])
def get_emojis():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM emojis;')
        emojis = cursor.fetchall()
        # will return emojis data and a 200 status code (successful)
        return jsonify({'emojis': emojis}), 200
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch emojis'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error fetching emojis from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# get emoji by emoji ID
@app.route('/fetch_emoji/<id>', methods=['GET'])
def get_emoji_by_id(id):
    connection = None
    cursor = None

    try:
        # connect to database
        connection = get_db_connection()
        cursor = connection.cursor()
        # query to select user by id
        cursor.execute('''SELECT id, emoji, label FROM emojis WHERE id = %s''', (id,))
        emoji = cursor.fetchone()
        if emoji is None:
            return jsonify({'error': f'Emoji with ID {id} not found'}), 404
        return jsonify({
            'id': emoji[0],
            'emoji': emoji[1],
            'label': emoji[2]
        }), 200

    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch emoji with that ID'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error fetching emoji with id {id} from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

###################### end of emojis ##########################

####################### mood logs ###############################

# fetches all mood logs from mood_logs table
@app.route('/mood_logs', methods=['GET'])
def get_mood_logs():
    connection = None
    cursor = None

    try: 
        connection = get_db_connection()
        cursor = connection.cursor()
        # query to join the mood_logs and emojis tables to get the emoji
        cursor.execute('''
            SELECT mood_logs.id, mood_logs.user_id, emojis.emoji, mood_logs.journal_entry, 
                   mood_logs.sentiment_score, mood_logs.created_at
            FROM mood_logs
            JOIN emojis ON mood_logs.emoji_id = emojis.id;
        ''')
        mood_logs = cursor.fetchall()
        # format the mood logs data
        mood_logs_list = [
            {
                'id': row[0],
                'user_id': row[1],
                'emoji': row[2],
                'journal_entry': row[3],
                'sentiment_score': row[4],
                'created_at': row[5]
            }
            for row in mood_logs          
        ]
        cursor.close()
        connection.close()
        return jsonify({'mood_logs': mood_logs_list}), 200
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch mood logs'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    except Exception as e:
        print(f'Unexpected error: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# creates a new mood log entry
@app.route('/add_mood_log', methods=['POST'])
def add_mood_log():
    connection = None
    cursor = None

    try:
        if request.method == 'POST':

            # gets the data from the request 
            data = request.get_json()

            # validates the required values
            if 'user_id' not in data or 'emoji_id' not in data:
                return jsonify({'error': 'Missing required values'}), 400
            
            # gets the required values from the request
            user_id = data['user_id']
            emoji_id = data['emoji_id']
            journal_entry = data.get('journal_entry', None)

            # gets the sentiment score from the OpenAI API
            def get_sentiment(journal_entry):
                try:
                    response = client.responses.create(
                    model="gpt-4o",
                    instructions="You are a sentiment analysis assistant. Analyze the sentiment of the following text and only return a score between -1 (very negative) and 1 (very positive).",
                    input=journal_entry
                    )
                    sentiment_score_text = response.output[0].content[0].text
                    # Convert the sentiment score to a float
                    sentiment_score = float(sentiment_score_text)
                    # Validate that the score is within the range of -1 to 1
                    if -1 <= sentiment_score <= 1:
                        return sentiment_score
                    else:
                        raise ValueError(f"Sentiment score {sentiment_score} is out of range.")
                except (ValueError, TypeError) as e:
                    print(f"Error: Invalid sentiment score - {e}")
                    return None
                except Exception as e:
                    print(f"Error: {e}")
                    return None

            # if the journal entry is not None, get the sentiment score
            if journal_entry is not None:
                # sets the sentiment score equal to the sentiment score from the OpenAI API
                sentiment_score = get_sentiment(journal_entry) 
                # If the sentiment score is invalid, return an error
                if sentiment_score is None:
                    return jsonify({'error': 'Invalid sentiment score'}), 400
            # if the journal entry is None, set the sentiment score to None
            else:
                sentiment_score = None

            # creates connection to the database
            connection = get_db_connection()
            cursor = connection.cursor()

            # query to insert the new mood log
            cursor.execute('''
                INSERT INTO mood_logs (user_id, emoji_id, journal_entry, sentiment_score)
                VALUES (%s, %s, %s, %s)
            ''', (user_id, emoji_id, journal_entry, sentiment_score))

            # commit changes
            connection.commit()
            return jsonify({'message': 'New mood log has been created!'}), 200

    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to create new mood log'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error adding mood log to the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# fetches a specific mood log by ID
@app.route('/get_mood_log/<int:id>', methods=['GET'])
def get_mood_log(id):
    connection = None
    cursor = None

    try:
        if request.method == 'GET':
            # connect to the database
            connection = get_db_connection()
            cursor = connection.cursor()
            # query to select the mood log by ID
            cursor.execute('''SELECT * FROM mood_logs WHERE id = %s;''', (id,))
            mood_log = cursor.fetchone()
            return jsonify({"mood_log": mood_log}), 200
        
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch mood log'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error fetching mood log from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# update an existing mood log by ID
@app.route('/update_mood_log/<int:id>', methods=['PUT'])
def update_mood_log(id):
    connection = None
    cursor = None

    try:
        # Parse the JSON data from the request
        data = request.get_json()
        emoji_character = data.get('emoji')  # User inputs the emoji character like 😀
        new_journal_entry = data.get('journal_entry', None)

        # Validate input
        if not emoji_character and new_journal_entry is None:
            return jsonify({"error": "At least one of 'emoji' or 'journal_entry' is required"}), 400

        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Get the emoji_id from the emojis table based on the emoji character
        new_emoji_id = None
        if emoji_character:
            cursor.execute('SELECT id FROM emojis WHERE emoji = %s', (emoji_character,))
            emoji_result = cursor.fetchone()
            if not emoji_result:
                return jsonify({"error": f"Emoji '{emoji_character}' not found"}), 400
            new_emoji_id = emoji_result[0]

        # Recalculate sentiment score if journal entry is updated
        new_sentiment_score = None
        if new_journal_entry is not None:
            # Function to calculate sentiment score
            def get_sentiment(journal_entry):
                try:
                    response = client.responses.create(
                        model="gpt-4o",
                        instructions="You are a sentiment analysis assistant. Analyze the sentiment of the following text and only return a score between -1 (very negative) and 1 (very positive).",
                        input=journal_entry
                    )
                    sentiment_score_text = response.output[0].content[0].text
                    sentiment_score = float(sentiment_score_text)
                    if -1 <= sentiment_score <= 1:
                        return sentiment_score
                    else:
                        raise ValueError(f"Sentiment score {sentiment_score} is out of range.")
                except (ValueError, TypeError) as e:
                    print(f"Error: Invalid sentiment score - {e}")
                    return None
                except Exception as e:
                    print(f"Error: {e}")
                    return None

            # Calculate the sentiment score
            new_sentiment_score = get_sentiment(new_journal_entry)
            if new_sentiment_score is None:
                return jsonify({'error': 'Failed to calculate sentiment score'}), 400

        # Build the SQL query dynamically based on the provided fields
        update_fields = []
        update_values = []

        if new_emoji_id is not None:
            update_fields.append("emoji_id = %s")
            update_values.append(new_emoji_id)

        if new_journal_entry is not None:
            update_fields.append("journal_entry = %s")
            update_values.append(new_journal_entry)

        if new_sentiment_score is not None:
            update_fields.append("sentiment_score = %s")
            update_values.append(new_sentiment_score)

        # Add the id to the values list for the WHERE clause
        update_values.append(id)

        # Construct and execute the SQL query
        update_query = f"UPDATE mood_logs SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(update_query, tuple(update_values))

        # Commit the changes
        connection.commit()

        # Close the database connection
        cursor.close()
        connection.close()

        return jsonify({'message': 'Mood log has been updated!'}), 200

    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
            print(f"ProgrammingError: {e}")
            return jsonify({'error': 'Failed to update mood log', 'details': str(e)}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        print(f"OperationalError: {e}")
        return jsonify({'error': 'Database connection failed', 'details': str(e)}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error updating mood log in the database: {e}')
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# delete a mood log by ID
@app.route('/delete_mood_log/<int:id>', methods=['DELETE'])
def delete_mood_log(id):
    connection = None
    cursor = None

    try:
        if request.method == 'DELETE':

            # connect to database
            connection = get_db_connection()
            cursor = connection.cursor()
            # query to delete mood log
            cursor.execute('''DELETE FROM mood_logs WHERE id = %s''', (id,))
            # commit changes
            connection.commit()
            return jsonify({'message': f'Mood log {id} has been deleted!'}), 200

    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': f'Failed to delete mood log {id}'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    # will catch any other errors
    except Exception as e:
        print(f'Error deleting mood log {id} from the database: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

##################### end of mood logs #############################

######################## articles ############################

# GET: Fetch articles from the database
@app.route('/articles', methods=['GET'])
def fetch_articles():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, title, category, link, author FROM articles;')
        rows = cursor.fetchall()
        articles = [
            {'id': row[0], 'title': row[1], 'category': row[2], 'link': row[3], 'author': row[4]}
            for row in rows
        ]
        cursor.close()
        connection.close()
        return jsonify({'articles': articles}), 200
    except Exception as e:
        print(f'Error fetching articles: {e}')
        return jsonify({'articles': []}), 500

# POST: Scrape articles and save to the database
@app.route('/scrape_articles', methods=['POST'])
def scrape_articles_route():
    try:
        url = 'https://www.verywellmind.com/self-improvement-4157212'
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            soup = BeautifulSoup(response.content, 'html.parser')
            titles = soup.find_all('span', class_='card__title-text')
            links = soup.find_all('a', class_="comp mntl-card-list-items mntl-document-card mntl-card card card--no-image")
            categories = soup.find_all('div', class_='card__content')
            authors = soup.find_all('div', class_='card__byline mntl-card__byline')
            if len(titles) == len(categories) == len(links) == len(authors):
                connection = get_db_connection()
                cursor = connection.cursor()
                cursor.execute('DELETE FROM articles;')
                for title, category, link, author in zip(titles, categories, links, authors):
                    category_title = category.get('data-tag', None)
                    link_href = link.get('href', None)
                    author_byline = author.get('data-byline', None)
                    if link_href and author_byline:
                        cursor.execute(
                            '''INSERT INTO articles (title, category, link, author) VALUES (%s, %s, %s, %s)''',
                            (title.text.strip(), category_title, link_href, author_byline)
                        )
                connection.commit()
                cursor.close()
                connection.close()
                return jsonify({'message': 'Articles scraped and saved!'}), 200
            else:
                return jsonify({'error': 'Mismatched lengths in scraped data lists'}), 500
        else:
            return jsonify({'error': f'Error fetching data from the URL: {response.status_code}'}), 500
    except Exception as e:
        print(f'Error scraping articles: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
########################### end of articles ############################

# route for the root URL
@app.route('/')
def index():
    return jsonify({'message': 'this is a message from the Flask backend!'}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)