from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Recette(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100))
    categorie = db.Column(db.String(100))
    contenu = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
