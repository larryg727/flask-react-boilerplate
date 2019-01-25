from api.app import models, db, bcrypt


def addUser(request):
    try:
        passwordHash = bcrypt.generate_password_hash(request.get('password'), 8)
        user = models.User(request.get('email'), passwordHash)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        if user.id:
            print(user.id)
            return True
        else:
            return False
    except Exception as e:
        print('Error occured during registration: ' + e)
        return False
