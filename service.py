from consts import user_table
from werkzeug.security import safe_str_cmp
import datetime

def authenticate(username, password):
    user = user_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user
    return None

def identity(payload):
    user = payload.get('identity')
    for k in user_table:
        if user_table[k].id == user.get('id'):
            return user_table[k]
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