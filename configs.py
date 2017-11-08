from flask import Flask
import datetime
import os
from peewee import *

# app init
app = Flask('app')
app.debug = True

# JWT settings
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=365)

# database settings
db = SqliteDatabase('app.db')

@app.before_request
def _db_connect():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()