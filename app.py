from flask import Flask, request
import json, datetime
from service import authenticate, identity, make_payload
from flask_jwt import JWT, jwt_required, current_identity
from configs import app

jwt = JWT(app, authenticate, identity)
jwt.jwt_payload_handler(make_payload(app))


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/show', methods=['GET'])
@jwt_required()
def show():
    id = request.args.get('id')
    if not id:
        id = 0
    r = {'success': True, 'content': 'abc{}'.format(id), 'identity': current_identity.username}
    return json.dumps(r)

