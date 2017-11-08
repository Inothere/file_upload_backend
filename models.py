from peewee import *
from configs import db

class User(Model):
    username = CharField()
    password = CharField()
    
    class Meta:
        database = db
    

