from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__, static_folder='../client/build/static', template_folder='../client/build')
APP.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:funnelai@localhost/project-x'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(APP)

from api.app import models
