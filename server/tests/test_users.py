import pytest
import psycopg2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture 
def sample_user():
    """ 
    create a sample user for testing

    returns: a dictionary with the test user's email and password
    """
    return {'email': 'test_user@test.com', 'password': 'testpassword'}

@pytest.fixture
def sample_users():
    """
    create multiple sample users for testing

    returns: a list of dictionaries with the test users' emails and passwords
    """
    return [
        {'email': 'steph@test.com', 'password': 'password123'},
        {'email': 'bob@test.com', 'password': 'password456'}]

@pytest.fixture
def duplicate_email_users():
    """
    create multiple sample users with a duplicate email for testing

    returns: a dictionary with the test users' email and password
    """
    return [
        {'email': 'dup_email@test.com', 'password': 'password123'},
        {'email': 'dup_email@test.com', 'password': 'password456'}]

@pytest.fixture
def client():
    """
    create a test client for the Flask app

    returns: a test client for the Flask app
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def reset_db():
    connection = psycopg2.connect(
        host="localhost",
        database="vibe_check",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        port="5432"
    )
    cursor = connection.cursor()
    cursor.execute('TRUNCATE TABLE users RESTART IDENTITY CASCADE;')
    connection.commit()
    cursor.close()
    connection.close()

def test_db_connection(db_connection):
    """
    test that the database connection is established and active

    args: 
      - db_connection: the database connection object
    asserts:
      - connection is not None
      - connection status is STATUS_READY
    """
    assert db_connection is not None
    assert db_connection.status == psycopg2.extensions.STATUS_READY

def test_insert_user(db_connection, sample_user):
    """
    test inserting a user into the users table

    args: 
      - db_connection: the database connection object
      - sample_user: a dictionary with the test user's email and password
    asserts:
      - user is not None
      - user has the correct email
      - user has the correct password
      - user has a valid id
      - user has a null OAuth_id (default)
      - user has a valid created_at timestamp
    """
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (email, password)"
                    "VALUES (%s, %s)",
                    (sample_user['email'], sample_user['password']))
    db_connection.commit()
    cursor.execute('SELECT * FROM users WHERE email = %s', (sample_user['email'],))
    user = cursor.fetchone()

    assert user is not None
    assert user[1] == sample_user['email']
    assert user[2] == sample_user['password']
    assert user[0] is not None
    assert user[3] is None 
    assert user[4] is not None

def test_programming_error(db_connection):
    """
    test that inserting a user with an invalid column raises a ProgrammingError

    args: 
      - db_connection: the database connection object
    raises:
      - psycopg2.ProgrammingError: non-existent column is referenced
    asserts:
      - the programming error is raised
      - the user is not inserted into the database
    """
    cursor = db_connection.cursor()
    with pytest.raises(psycopg2.ProgrammingError):
        cursor.execute("INSERT INTO users (non_existent_column, password)"
                        "VALUES (%s, %s)",
                        ('test@test.com','strongpassword123'))
        db_connection.commit()
    db_connection.rollback()
    cursor.execute('SELECT * FROM users WHERE email = %s',('test@test.com',))
    user = cursor.fetchone()

    assert user is None

def test_fetch_users(db_connection, sample_users):
    """ 
    will test fetching all users from the users table to ensure that the database is returning the correct data 

    args:
      - db_connection: the database connection object
      - sample_users: a list of dictionaries with the test users' emails and passwords
    asserts:
      - all users (2) were fetched successfully
      - the first user has the correct email
      - the second user has the correct email
      - the first user has a valid id
      - the second user has a valid id
      - non-existent user does not exist
    """
    cursor = db_connection.cursor()
    # loop through sample data of users and inserts them into table
    for user in sample_users:
      cursor.execute("INSERT INTO users (email, password)"
                    "VALUES (%s, %s)",
                    (user['email'], user['password']))
    db_connection.commit()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    assert len(users) == 2
    assert users[0][1] == sample_users[0]['email']
    assert users[1][1] == sample_users[1]['email']
    assert users[0][0] is not None
    assert users[1][0] is not None

def test_fetch_user_by_id(db_connection, sample_users):
    """ 
    will test fetching a user by their ID from the users table 

    args:
      - db_connection: the database connection object
      - sample_users: a list of dictionaries with the test users' emails and passwords
    asserts:
      - user is not None
      - user has the correct ID
      - user has the correct email
      - user has the correct password
      - user has a valid created_at timestamp
    """
    cursor = db_connection.cursor()
    # loop through sample data of users and inserts them into table
    for user in sample_users:
      cursor.execute("INSERT INTO users (email, password)"
                    "VALUES (%s, %s)",
                    (user['email'], user['password']))
    db_connection.commit()

    cursor.execute('SELECT id FROM users WHERE email = %s', (sample_users[0]['email'],))
    user_id = cursor.fetchone()[0]
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    fetched_user = cursor.fetchone()

    assert fetched_user is not None
    assert fetched_user[0] == user_id
    assert fetched_user[1] == sample_users[0]['email']
    assert fetched_user[2] == sample_users[0]['password']

def test_update_user(db_connection, sample_user):
    """
    test updating a sample user's password in the users table

    args:
      - db_connection: the database connection object
      - sample_user: a dictionary with the test user's email and password
    asserts:
      - user is not None
      - user has the correct email
      - user has the updated password
    """
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (email, password)"
                    "VALUES (%s, %s)",
                    (sample_user['email'], sample_user['password']))
    db_connection.commit()
    cursor.execute("UPDATE users SET password = %s WHERE email = %s", 
                  ('newpassword', sample_user['email'],))
    db_connection.commit()
    cursor.execute('SELECT * FROM users WHERE email = %s', (sample_user['email'],))
    updated_user = cursor.fetchone()

    assert updated_user is not None
    assert updated_user[1] == sample_user['email']
    assert updated_user[2] == 'newpassword'

def test_delete_user(db_connection, sample_user):
    """
    test deleting a sample user from the users table

    args:
      - db_connection: the database connection object
      - sample_user: a dictionary with the test user's email and password
    asserts:
      - user is None
    """
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (email, password)"
                    "VALUES (%s, %s)",
                    (sample_user['email'], sample_user['password']))
    db_connection.commit()
    cursor.execute("DELETE from users WHERE email = %s",
                  (sample_user['email'],))
    db_connection.commit()
    cursor.execute('SELECT * FROM users WHERE email = %s', (sample_user['email'],))
    deleted_user = cursor.fetchone()

    assert deleted_user is None

def test_insert_duplicate_email(client, duplicate_email_users, reset_db):
    """
    test inserting a user with a duplicate email into the users table

    args:
      - client: the test client for the Flask app
      - duplicate_email_users: a list of dictionaries with the test users' emails and passwords
      - reset_db: a fixture to reset the database before each test
    asserts:
      - unique constraint error is raised
      - the first user is inserted into the database
      - user with duplicate email is not inserted into the database
    """
    response = client.post('/register', json=duplicate_email_users[0])
    assert response.status_code == 200
    assert response.get_json() == {'message': 'new user has been created!'}

    # try to insert the second user with a duplicate email
    response = client.post('/register', json=duplicate_email_users[1])
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Email already exists'}

def test_insert_empty_email(client):
    """
    test inserting a user with an empty email into the users table

    args:
      - client: the test client for the Flask app
    asserts:
      - check 'missing required fields' error and 400 status code is raised
    """
    response = client.post('/register', json={'email': '', 'password': 'testpassword'})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Missing required fields'}

def test_insert_empty_password(client):
    """
    test inserting a user with an empty password into the users table

    args:
      - client: the test client for the Flask app
    asserts:
      - check 'missing required fields' error and 400 status code is raised
    """
    response = client.post('/register', json={'email': 'test123@test.com', 'password': ''})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Missing required fields'}