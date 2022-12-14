from flask import Blueprint, request

BP = Blueprint('user', __name__)
from schemas.user import user_schema
from models.user import User
from initial.init_database import db

@BP.route('/')
def index():
    data = request.get_json()
    user_schema.load(data)
    return user_schema.dump(User.query.get(0))


@BP.route('/create_user', methods=['POST'])
def create_user():
    data = request.data
    user = User(name='linh', email='linh@gmail.com')
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)
