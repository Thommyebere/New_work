import database
import datetime
import os
import psycopg2
from dotenv import load_dotenv
import database
import getpass

import items

load_dotenv()
database_uri = os.environ["DATABASE_URI"]

connection = psycopg2.connect(database_uri)


class Users(object):

    def __init__(self):
        pass

    @staticmethod
    def sign_up(connection):
        firstname = input("Enter your first name ")
        lastname = input("Enter your last name ")
        password = input("Enter your password ")
        status = input("Enter your access code")
        date = datetime.datetime.now()
        if status == '256':
            status = 'admin'
        else:
            status = 'customer'
        database.create_user(connection, firstname, lastname, password, status, date)

    @staticmethod
    def login(connection):
        first_name = input("Enter your firstname ")
        pass_word = getpass.getpass(prompt='Enter password')
        if database.login_user(connection, first_name):
            stats, password = database.login_user(connection, first_name)
            if password == pass_word and stats == 'admin':
                print("Test is gotten ")

            elif password == pass_word and stats != 'admin':
                print("second ack ")

            else:
                print("please check your password ")
        else:
            print("Your username does not exist")
            dev.sign_up(connection)


dev = Users()
dev.login(connection)
# dev.sign_up(connection)
