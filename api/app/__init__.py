import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db_uri

# Initiate Flask app and set template and static folder to React's build folder to enable server to send front end files
app = Flask(__name__, static_folder='../client/build/static',
            template_folder='../client/build')
# Configure apps db with uri and settings
app.config['SQLALCHEMY_DATABASE_URI'] = '{0}/{1}'.format(
    db_uri, os.getenv('DB_NAME'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize DB
db = SQLAlchemy(app)
# Import models - Must remain after db initialization
from api.app import models
