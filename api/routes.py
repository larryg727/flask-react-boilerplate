from flask import jsonify, request, render_template
from api.app import APP


@APP.route('/')
def index():
    '''
    Returns index.html from react production bundle
    '''
    print('hello')
    return render_template('index.html')


@APP.route('/api/test')
def test():
    '''
    returns test data for api test
    '''
    return jsonify({'test': 'API works'})
