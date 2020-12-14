import os
import psycopg2
from dotenv import load_dotenv
import database
import datetime
from items import Items

load_dotenv()
database_uri = os.environ["DATABASE_URI"]

connection = psycopg2.connect(database_uri)
database.create_tables(connection)


class Choices(object):
    def __init__(self):
        choice = """
        1. Press 1 to add items
        2. Press 2 to check items that are sold out
        3. Press 3 to check for sold items 
        4. Press 4 to update inventory 
        """
        self.mychoice = int(input(choice))

    def selection(self):
        if self.mychoice == 1:
            Items.add_items(connection)

        elif self.mychoice == 2:
            Items.sold_out_item(connection)

        elif self.mychoice == 3:
            Items.sold_items(connection)

        elif self.mychoice == 4:
            Items.update_inventory(connection)

        else:
            print("Invalid input ")

option = Choices()
option.selection()
