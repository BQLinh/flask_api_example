from flask_marshmallow import Schema


class UserSchema(Schema):
    class Meta:
        fields = ['id', 'name', 'age']


user_schema = UserSchema()
