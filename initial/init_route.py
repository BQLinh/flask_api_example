from routes import user, auth


def init_app(app):
    app.register_blueprint(user.BP, url_prefix='/')
    app.register_blueprint(auth.BP, url_prefix='/')