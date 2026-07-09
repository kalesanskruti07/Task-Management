from app.models import User


def user_exists(email):
    return User.query.filter_by(email=email).first()