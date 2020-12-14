from users import Users
import database
import datetime
import os
import psycopg2
from dotenv import load_dotenv
import database

load_dotenv()
database_uri = os.environ["DATABASE_URI"]

connection = psycopg2.connect(database_uri)


class Glass(object):
    def __init__(self):
        pass


user = Glass()
Users.sign_up(connection)
