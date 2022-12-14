from routes import user, auth, blog


def init_app(app):
    app.register_blueprint(user.BP, url_prefix='/')
    app.register_blueprint(auth.BP, url_prefix='/')
    app.register_blueprint(blog.BP, url_prefix='/')