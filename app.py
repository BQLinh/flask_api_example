from flask import Flask
from dotenv import load_dotenv
import models
import os
from initial import init_database, init_schema, init_route


app_env = os.environ.get('FLASK_ENV', default='development')

print(os.environ)
if app_env == 'test':
    load_dotenv('.env.test')
else:
    load_dotenv('.env')

print(app_env)

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI')
# app.config.from_object(config)

init_database.init_app(app)
init_schema.init_app(app)
init_route.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
