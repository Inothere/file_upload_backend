from models import User
from werkzeug.security import safe_str_cmp
import datetime

def authenticate(username, password):
    try:
        query_results = User.select().where(User.username==username)
        user = query_results[0] if query_results else None
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user
        return None
    except User.DoesNotExist:
        return None

def identity(payload):
    user_obj = payload.get('identity')
    try:
        return User.get(User.username == user_obj.get('name'))
    except User.DoesNotExist:
        return None

def make_payload(app): 
    def func(identity):
        iat = datetime.datetime.utcnow()
        exp = iat + app.config.get('JWT_EXPIRATION_DELTA')
        nbf = iat + app.config.get('JWT_NOT_BEFORE_DELTA')
        new_identity = {
            'id': identity.id,
            'name': identity.username,
            'pwd': identity.password
        }
        return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': new_identity}
    return func