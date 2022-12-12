from models.user import User

def check_dupplicate_email(email):
    users = User.query.filter_by(email=email).count()

    if users == 0:
        return False
    return True