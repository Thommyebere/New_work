import os
import psycopg2
from dotenv import load_dotenv
import database
import datetime

load_dotenv()
database_uri = os.environ["DATABASE_URI"]

connection = psycopg2.connect(database_uri)
database.create_tables(connection)
import fpdf as fpdf


class Items(object):
    def __init__(self):
        pass

    @staticmethod
    def add_items(connection):
        item_name = input("Enter the name of the item ")
        item_quantity = input("Enter item quantity ")
        item_price = input("Enter item price  ")
        date = datetime.datetime.now()
        database.create_item(connection, item_name, item_quantity, item_price, date)


    @staticmethod
    def buy_item(connection):
        uuid = 1234
        session = True
        while database.buy_item(connection) is not None:
            item_search = database.buy_item(connection)
            print("---------------->Welcome<------------------")
            print("Items             |             price")
            for items in item_search:
                print("{}             |             ${}".format(items[0], items[2]))
            item_choice = input("What item do you want to buy? ")
            if item_choice != "":
                item_choice_qty = int(input("Enter item quantity "))
                for item in item_search:
                    if item_choice in item:
                        print(item[1])
                        if item[1] < item_choice_qty:
                            print(item[1])
                            print(item_choice_qty)
                            print("We only have {} in store. Buy these. Thank you!".format(item[1]))
                            total_price = item[2] * item[1]
                            print(total_price)
                            database.create_item_log(connection, item_choice, item[1], item[2], total_price, uuid,
                                                     date=datetime.datetime.now())
                            item = list(item)
                            item[1] = 0
                            database.set_item_table(connection, item[1], item_choice)
                            print("Transaction successful ")
                        else:
                            total_price = item_choice_qty * item[1]
                            database.create_item_log(connection, item_choice, item_choice_qty, item[2], total_price,
                                                     uuid,
                                                     date=datetime.datetime.now())
                            item = list(item)
                            item[1] = item[1] - item_choice_qty
                            database.set_item_table(connection, item[1], item_choice)
                            print("Transaction successful ")

                    else:
                        pass
            else:
                receipts = database.item_receipts(connection, uuid)
                pdf = fpdf.FPDF(format='letter')
                pdf.add_page()
                pdf.set_font("Arial", size=7)

                t = len(receipts)
                for i in receipts:
                    pdf.write(t, str(i))
                    pdf.ln()
                pdf.output("testings.pdf")

    @staticmethod
    def sold_out_item(connection):
        items = database.out_of_stock(connection)
        for item in items:
            print(item[0], item[1], item[2], item[3], item[4])

    @staticmethod
    def sold_items(connection):
        sold_items = database.sold_items(connection)
        for item in sold_items:
            print(item[0], item[1], item[2], item[3], item[4], item[5])

    @staticmethod
    def update_inventory(connection):
        item_name = input("Enter the name of the item ")
        item_search = database.all_items(connection)

        def table():
            for item in item_search:
                if item_name in item:
                    return item_name
                else:
                    pass

        if table() is not None:
            item_quantity = int(input("Enter the quantity of the item "))
            database.set_item_table(connection, item_quantity, item_name)
        else:
            item_quantity = input("Enter item quantity ")
            item_price = input("Enter item price  ")
            date = datetime.datetime.now()
            database.create_item(connection, item_name, item_quantity, item_price, date)


# print("ITEM                 |       QUANTITY                |               TOTAL")
# for goods in receipts:
#     print("{}               |               {}                  {}".format(goods[0], goods[1], goods[2]))


# Items.add_items(connection)
# Items.sold_out_item(connection)
# Items.sold_items(connection)
# Items.update_inventory(connection)

# Items.display_items(connection)
# Items.buy_item(connection)

# t = [('J', 10), ('K', 10)]
#
# for x in t:
#     x = list(x)
#     x[1] = 1
#     print(x)
