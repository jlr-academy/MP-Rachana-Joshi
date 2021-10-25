from dotenv import load_dotenv
import pymysql
import sys
import csv
import os
from os import system
from typing import DefaultDict, List, Dict, Sequence
from types import new_class

def export_products_to_csv_d():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    cursor = connection.cursor()

    cursor.execute('SELECT product_id, product_name, product_price, units FROM products')

    rows = cursor.fetchall()
    with open("products_db", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for row in rows:
            csvwriter.writerow(row) 
    cursor.close()

    connection.close()   

def export_couriers_to_csv_d():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    cursor = connection.cursor()

    cursor.execute('SELECT courier_id, courier_name, courier_phone FROM couriers')

    rows = cursor.fetchall()
    with open("couriers_db", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for row in rows:
            csvwriter.writerow(row)            

#     cursor.close()

#     connection.close()