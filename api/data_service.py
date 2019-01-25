from api.app import models, db

def addUser(request):
    user = models.User(request.get('email'), request.get('password'))
    db.session.add(user)
    db.session.commit()
    return True