from flask_marshmallow import Schema, fields

from .user import UserSchema
from models.blog import Blog
from initial.init_schema import ma

class BlogSchema(Schema):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'content']
    
    author = ma.Nested(UserSchema)
blog_schema = BlogSchema()

