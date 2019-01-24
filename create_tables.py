from api.app import APP, db

with APP.app_context():
    db.create_all()