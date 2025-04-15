from flask import Flask
from flask_cors import CORS

import os
import psycopg2
# loads environment variables from a .env file
from dotenv import load_dotenv

# creates Flask app instance
app = Flask(__name__)

# creates a connection to the PostgreSQL database
# using environment variables for credentials
def get_db_connection():
    # loads environment variables from .env file
    load_dotenv()
    connection = psycopg2.connect(
        host="localhost",
        database="vibe_check",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        port="5432")
    return connection

# route to test the users table connection
@app.route('/users')
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return {
        'users': users
    }

# route to test the mood logs table connection
@app.route('/mood_logs')
def get_mood_logs():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mood_logs;')
    mood_logs = cursor.fetchall()
    cursor.close()
    connection.close()
    return {
        'mood_logs': mood_logs
    }


# enables cross-origin requests for all routes
cors = CORS(app, origins='*')

# creates a route for the root URL
@app.route('/')
def index():
    return {
        'message': 'this is a message from the Flask backend!'
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)