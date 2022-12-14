from initial.init_database import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User',  back_populates="blog")
    title = db.Column(db.String(128))
    content = db.Column(db.String(256))


class BlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(128))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    blog = db.relationship('Blog', backref='blog_comment')
