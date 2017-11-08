from configs import db
from models import *

tables = [User]
db.create_tables(tables)