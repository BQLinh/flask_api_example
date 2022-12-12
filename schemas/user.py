from flask_marshmallow import Schema


class UserSchema(Schema):
    class Meta:
        fields = ['id', 'name']


user_schema = UserSchema()
