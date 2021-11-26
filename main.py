import os
from app import create_app
from flask import request, Response, jsonify
from flask_pymongo import PyMongo
import bson
from routes import *

app = create_app()

mongo = PyMongo(app)

app.register_blueprint(routes)

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'name':'API', 'version':'v1'})

if __name__ == "__main__":
    app.run(port = 4500, debug=True)

