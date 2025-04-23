from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import psycopg2
# loads environment variables from a .env file
from dotenv import load_dotenv

# creates Flask app instance
app = Flask(__name__)
# enables cross-origin requests for all routes
cors = CORS(app, origins='*')

# creates a connection to the PostgreSQL database
# using environment variables for credentials
def get_db_connection():
    try:
        # loads environment variables from .env file
        load_dotenv()
        connection = psycopg2.connect(
            host="localhost",
            database="vibe_check",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'],
            port="5432")
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
@app.route('/get_users', methods=['GET'])
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
        if connection:
            connection.close()
        if cursor:
            cursor.close()

# creates a new user 
@app.route('/add_user', methods=['POST'])
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
            # query to insert new user
            cursor.execute('''INSERT INTO users (email, password) VALUES (%s , %s)''', (email, password))
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
        if connection:
            connection.close()
        if cursor:
            cursor.close()

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
        if connection:
            connection.close()
        if cursor:
            cursor.close()

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
                return jsonify({"error": "Email and password are required"}), 500
            
            # connect to database
            connection = get_db_connection()
            cursor = connection.cursor()
            # query to insert new user
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
        if connection:
            connection.close()
        if cursor:
            cursor.close()

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
        if connection:
            connection.close()
        if cursor:
            cursor.close()

##################### end of users ##################################

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
        if connection:
            connection.close()
        if cursor:
            cursor.close()

# fetches all mood logs from mood_logs table
@app.route('/mood_logs', methods=['GET'])
def get_mood_logs():
    connection = None
    cursor = None

    try: 
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM mood_logs;')
        mood_logs = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify({'mood_logs': mood_logs}), 200
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
        if connection:
            connection.close()
        if cursor:
            cursor.close()
            

# fetches all articles from articles table
@app.route('/articles', methods=['GET'])
def get_articles():
    connection = None
    cursor = None

    try: 
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM articles;')
        articles = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify({'articles': articles}), 200
    # error handling for SQL syntax errors, invalid table/columns, incorrect data types, etc
    except psycopg2.ProgrammingError:
        return jsonify({'error': 'Failed to fetch articles'}), 500
    # error handling for connection failure, invalid DB name/credentials, networking issues, etc.
    except psycopg2.OperationalError:
        return jsonify({'error': 'Database connection failed'}), 500
    except Exception as e:
        print(f'Unexpected error: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()
            

# route for the root URL
@app.route('/')
def index():
    return jsonify({'message': 'this is a message from the Flask backend!'}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)