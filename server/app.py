from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# creates Flask app instance
app = Flask(__name__)

# configures the app to use SQLAlchemy with PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tpl1122_15@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# creates SQLAlchemy instance
db = SQLAlchemy(app)

# defines a User model for the database
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    OAuth_id = db.Column(db.String)
    created_at = db.Column(db.DateTime)

# enables cross-origin requests for all routes
cors = CORS(app, origins='*')

# creates a route for the root URL
@app.route('/')
def index():
    return {
        'message': 'this is a message from the Flask backend!'
    }

# route to test the users table connection
@app.route('/users')
def get_users():
    users = User.query.all()
    return '<br>'.join([f'{u.id}: {u.email}' for u in users])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)