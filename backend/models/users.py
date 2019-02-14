from backend.extensions import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
