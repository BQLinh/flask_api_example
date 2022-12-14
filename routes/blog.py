from flask import Blueprint, request

BP = Blueprint('blog', __name__)

from initial.init_database import db
from models.blog import Blog, BlogComment
from models.user import User
from schemas.blog import blog_schema

from services.jwt_token import JWT_Token


@BP.route('/blog', methods=['POST'])
def create_user():
    data = request.data
    blog = Blog(title='this blog', content='this content', author_id=1)
    db.session.add(blog)
    db.session.commit()
    return blog_schema.dump(blog)


@BP.route('/blog', methods=['GET'])
def get_blog():
    blog = Blog.query.first()
    author = blog.author

    # user = User.query.first()
    # blog.user = user
    print(author)
    print(blog)

    user = User.query.first()
    print(user.blog)
    # db.session.
    db.session.commit()
    return blog_schema.dump(blog)

@BP.route('/blog_detail', methods=['GET'])
def blog_detail():

    blog = Blog(title='this blog', content='this content', author_id=1)
    db.session.add(blog)
    db.session.commit()

    blog_detail = BlogComment(comment='adadasd', blog=blog)
    
    db.session.add(blog_detail)
    db.session.commit()
    blog = blog_detail.blog
    print(blog)
    # blog_comments = blog.blogcomment
    print(blog.blog_comment)

    return blog_schema.dump(blog_detail)
