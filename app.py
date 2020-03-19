from flask import Flask, jsonify, send_file
from flask_cors import CORS 
import sqlite3

app = Flask(__name__)
# enable the api to be accessed by frontend running on localhost
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1"}})

# define what to do when the user navigates to "/"
# this serves a static html file. 
@app.route('/')
def index():
    return send_file("static/html/index.html")

# our mock data - like what we could get from a database
db_connection = sqlite3.connect('restaurants.db')
db_cursor = db_connection.cursor()
db_cursor.execute("SELECT * from restaurants WHERE NEIGHBORHOOD_ID = 1")
restaurants = db_cursor.fetchall()
db_connection.close()
print(restaurants)

# A HTTP RESTful API Route returning the full restaurants dictionary
@app.route('/api/restaurants/all',  methods=['GET'])
def api_restaurants_all():
    return jsonify(restaurants)

# A HTTP RESTful API Route returning a list of names of restaurants

@app.route('/api/restaurants/names',  methods=['GET'])
def api_restaurants_names():
    # create a new list
    restaurant_names = []
    # loop through the data, adding the names of each restaurant to our new list 
    for restaurant in restaurants: 
        restaurant_names.append(restaurant[1])
    return jsonify(restaurant_names)



# Run this application if the file is executed, e.g. as "python3 backend.py" 
if __name__ == '__main__': 
    app.testing=True
    app.run()