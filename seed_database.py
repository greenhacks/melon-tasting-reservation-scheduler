""""Automatically populates the database with sample data"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
from model import connect_to_db, db
import server


# executes command line code in console
os.system('dropdb melon-tasting-scheduler-db')
os.system('createdb melon-tasting-scheduler-db')

# connects to the database 
connect_to_db(server.app, 'melon-tasting-scheduler-db')

# creates tables
db.create_all()

email = 'user1@test.com'

db_email = crud.create_user(email)