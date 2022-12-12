from flask_marshmallow import Schema
from models.user import User

class AuthSchema(Schema):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


auth_schema = AuthSchema()
