from functools import wraps
from flask import request
from models.user import User
from .jwt_token import JWT_Token


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1]

        jwt_token = JWT_Token()
        result = jwt_token.check_token(token)
        if 'error' in result:
            return {
                "result": result['error']
            }
        return f(*args,**kwargs)
    return decorated
