CREATE_USER = """CREATE TABLE IF NOT EXISTS users
(id SERIAL PRIMARY KEY,first_name TEXT,last_name TEXT,password TEXT, status TEXT,date Date);"""
CREATE_ITEMS = """CREATE TABLE IF NOT EXISTS items
(id SERIAL PRIMARY KEY,item TEXT, quantity INTEGER, price INTEGER,date DATE);"""
MAKE_ORDERS = """CREATE TABLE IF NOT EXISTS orders
(id SERIAL PRIMARY KEY,item TEXT, quantity INTEGER, price INTEGER,date DATE);"""
CREATE_ITEM_STOCK = """CREATE TABLE IF NOT EXISTS item_stock (id SERIAL PRIMARY KEY,item TEXT,quantity INTEGER, 
price_for_one INTEGER, total INTEGER, user_id INTEGER, date DATE); """
CREATE_PURCHASE_HISTORY = """CREATE TABLE IF NOT EXISTS history
(id SERIAL PRIMARY KEY, item TEXT, price INTEGER, date DATE); """

SELECT_USER_LOGIN = "SELECT status,password from users where first_name= %s;"
SELECT_ALL_ITEMS = "SELECT item,quantity,price FROM items where quantity>0"
SELECT_ITEMS_BOUGHT = "SELECT item, quantity,total FROM item_stock WHERE user_id=%s;"
SELECT_ALL_ITEMS_OUT_OF_STOCK = "SELECT * FROM items where quantity<=0"
SELECT_SOLD_ITEMS="SELECT * FROM item_stock"
SELECT_ALL_ITEMSS="SELECT * FROM items"

INSERT_USER = "INSERT INTO users(first_name, last_name,password,status,date) VALUES (%s,%s,%s,%s,%s);"

INSERT_ITEM = "INSERT INTO items (item, quantity,price,date) VALUES (%s,%s,%s,%s);"

INSERT_BOUGHT_ITEM = "INSERT INTO item_stock (item, quantity,price_for_one, total,user_id,date) VALUES(%s,%s," \
                     "%s,%s,%s,%s); "
UPDATE_ITEM_QUANTITY = "UPDATE items SET quantity=%s where item=%s"




def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USER)
            cursor.execute(CREATE_ITEMS)
            cursor.execute(MAKE_ORDERS)
            cursor.execute(CREATE_ITEM_STOCK)
            cursor.execute(CREATE_PURCHASE_HISTORY)


def create_user(connection, first_name, last_name, password, status, date):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (first_name, last_name, password, status, date))


def create_item(connection, item_name, item_quantity, item_price, date):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_ITEM, (item_name, item_quantity, item_price, date))


def create_item_log(connection, item, quantity, price_for_one, total, user_id, date):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_BOUGHT_ITEM, (item, quantity, price_for_one, total, user_id, date))


def item_receipts(connection, num):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ITEMS_BOUGHT, (num,))
            return cursor.fetchall()


def set_item_table(connection, quantity, item):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(UPDATE_ITEM_QUANTITY, (quantity, item))


def buy_item(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_ITEMS)
            return cursor.fetchall()

def all_items(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_ITEMSS)
            return cursor.fetchall()

def login_user(connection, first_name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_USER_LOGIN, (first_name,))
            return cursor.fetchone()


def out_of_stock(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_ITEMS_OUT_OF_STOCK)
            return cursor.fetchall()

def sold_items(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_SOLD_ITEMS)
            return cursor.fetchall()

