from app.models.user import User
from app import db

class UserService:
    
    @staticmethod
    def getUserById(userId):
        return User.query.get(userId)
    
    @staticmethod
    def getAllUsers():
        return User.query.all()
    
    @staticmethod
    def createUser(name, email, password, userType, speciality):
        newUser = User(
            name       = name,
            email      = email,
            password   = password,
            userType   = usertype,
            speciality = speciality
        )
        db.session.add(newUser)
        db.session.commit()
        return newUser
    
    @staticmethod
    def updateUser(userId, **kwargs):
        user = User.query.get(userId)
        if not user:
            return None
        
        for key, value in kwargs.items():
            setattr(user, key, value)
        
        db.session.commit()
        return user
    
    @staticmethod
    def deleteUser(userId):
        user = User.query.get(userId)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user