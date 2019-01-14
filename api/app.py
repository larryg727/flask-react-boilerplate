from flask import Flask

APP = Flask(__name__, static_folder='../client/build/static', template_folder='../client/build')
