from initial.init_database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    is_active = db.Column(db.Boolean)
    password = db.Column(db.String(256))
    age = db.Column(db.Integer)
    blog = db.relationship('Blog', back_populates='author')