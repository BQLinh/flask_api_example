from flask import Flask

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app2.db'
app.config.from_envvar('ENV_FILE_LOCATION')

import models

from initial import init_database, init_schema, init_route

init_database.init_app(app)
init_schema.init_app(app)
init_route.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
