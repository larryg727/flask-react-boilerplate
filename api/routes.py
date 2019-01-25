from flask import jsonify, request, render_template
from api.app import app
from api import data_service


@app.route('/')
def index():
    '''
    Returns index.html from react production bundle
    '''
    print('hello')
    return render_template('index.html')


@app.route('/api/test')
def test():
    '''
    returns test data for api test
    '''
    return jsonify({'test': 'API works'})


@app.route('/api/register', methods=['POST'])
def register():
    # TODO: add password hashing before save and error handleing
    result = data_service.addUser(request.form)
    return jsonify({'success': result})
