from flask import Flask
from flask_cors import CORS

# creates Flask app instance
app = Flask(__name__)

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