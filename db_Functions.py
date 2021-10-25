from logging import exception
import os
from os import system
from types import new_class
from typing import List, Dict, Sequence
from dotenv import load_dotenv
import pymysql
#import MySQLdb

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    #system("cls")

def print_products_d():
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
    print("\n{:<1} {:<15} {:<20} {:<15} {:<13}".format("","Product Id","Product Name","Product Price","Product Stock"))
    for row in rows:
        print("{:<1} {:<15} {:<20} {:>13} {:>15}".format("",row[0],row[1],row[2],row[3]))
    cursor.close()
    connection.close()

def create_product_d():
    product_name = input("Enter a new product: ")
    if product_name:
        product_name = product_name.capitalize()
        try:
            product_price=float(input("Enter product price: "))
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
            try:
                sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
                val = (product_name, product_price)
                cursor.execute(sql, val)
                connection.commit()
            except Exception as e:
                print(e)        
            cursor.close()
            connection.close()
        except ValueError as e:
            print(f"\nInvalid input: only numbers allowed, {e}")
    else:
        print("\nProduct name cannot be blank")
            
def update_product_d():
    updated = []
    i=0
    a = 0 
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
    #########################################################
    cursor.execute('SELECT product_id, product_name, product_price FROM products')
    rows = cursor.fetchall()
    print("\n{:<1} {:<15} {:<20} {:<10}".format("","Product_Id","Product Name","Product Price"))
    for row in rows:
        print("{:<1} {:<15} {:<20} {:<10}".format("",row[0],row[1],row[2]))
    try:
        p_index = int(input("\nPlease enter Product Id to update: "))
    except Exception as e:
        print(f"\nInvalid input,{e}")
    sql = "SELECT product_id, product_name, product_price FROM products where product_id = %s"
    val = (p_index)
    cursor.execute(sql, val)
    row = cursor.fetchone()
    if row == None:
            print("\nInvalid input, product id not found")
            a = 1
    else:        
        print("\nCurrent value is:",row[1])
        new_name = input("Please press enter to retain value or enter new name:  ")
        new_name = new_name.capitalize()
        print("\nCurrent value is: ",row[2])
        new_price = 0
        try:
            new_price = float(input("Please enter 0 to retain value or enter new price:  "))
        except Exception as e:
            print(f"\nInvalid input: price retained")
            a = 1
        if new_name == "":
            new_name = row[1] 
        if new_price == 0:
            new_price = row[2]
        sql = "UPDATE products set product_name = %s, product_price = %s where product_id = %s"
        val = (new_name, new_price, p_index)
        try:
            cursor.execute(sql, val)
            connection.commit()
        except Exception as e:
            print(f"\n {e}") 
            a = 1   
    cursor.close()
    connection.close()
    if a == 0:
        print('\nProduct successfully updated') 

def delete_product_d():
    a = 0 
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
    #########################################################
    cursor.execute('SELECT product_id, product_name, product_price FROM products')
    rows = cursor.fetchall()
    print("\n{:<1} {:<15} {:<20} {:<10}".format("","Product Id","Product Name","Product Price"))
    for row in rows:
        print("{:<1} {:<15} {:<20} {:<10}".format("",row[0],row[1],row[2]))
    while True:
        try:
            p_index = int(input("\nPlease enter product_id to delete: "))
            sql = "SELECT product_id FROM products where product_id = %s"
            cursor.execute(sql, p_index)            
            rows = cursor.fetchall() 
            if len(rows) == 0:
                print("Product does not exists") 
            else:              
                break
        except Exception as e:
            print(f'{e},\nInvalid input')
    confirm = input("Are you sure? Y/N:   ")
    if confirm.capitalize() == 'Y':
        sql = "DELETE from products where product_id = %s"
        val = (p_index)
    #########################################################
        try:
            cursor.execute(sql, val)
            connection.commit()
            print("\nProduct successfully deleted")
        except Exception as e:
            print(e)
    elif confirm.capitalize() == 'N':
        print("\nProduct not deleted")
    else:
        print("\nInvalid choice")    
    cursor.close()
    connection.close()
    
def print_courier_d():
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
    print("\n{:<1} {:<15} {:<20} {:<15}".format("","Courier Id","Courier Name","Courier Phone"))
    for row in rows:
        print("{:<1} {:<15} {:<20} {:>13}".format("",row[0],row[1],row[2]))
    cursor.close()
    connection.close()

def create_courier_d():
    courier_name = input("Enter a new courier: ")
    if courier_name:
        courier_name = courier_name.capitalize()
        courier_phone = '0'
        try:
            #courier_phone=input("Enter a valid 10 digit phone number: ")
            while len(courier_phone) != 11 or not courier_phone.isdigit():
                courier_phone=input("Enter a valid 10 digit phone number: ")
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
            try:
                sql = "INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)"
                val = (courier_name, courier_phone)
                cursor.execute(sql, val)
                connection.commit()
            except Exception as e:
                print(e)        
            cursor.close()
            connection.close()
        except ValueError as e:
            print(f"Invalid input: only numbers allowed")
    else:
        print("Courier name cannot be blank")
            
def update_courier_d():
    updated = []
    i=0
    a = 0 
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
    #########################################################
    cursor.execute('SELECT courier_id, courier_name, courier_phone FROM couriers')
    rows = cursor.fetchall()
    print("\n{:<1} {:<15} {:<20} {:<10}".format("","Courier Id","Courier Name","Courier Phone"))
    for row in rows:
        print("{:<1} {:<15} {:<20} {:<10}".format("",row[0],row[1],row[2]))
    try:
        c_index = int(input("\nPlease enter Courier Id to update: "))
    except Exception as e:
        print(f"\nInvalid input,{e}")
    sql = "SELECT courier_id, courier_name, courier_phone FROM couriers where courier_id = %s"
    val = (c_index)
    cursor.execute(sql, val)
    row = cursor.fetchone()
    if row == None:
            print("\nInvalid input, courier id not found")
            a = 1
    else:        
        print("\nCurrent value is:",row[1])
        new_name = input("Please press enter to retain value or enter new name:  ")
        new_name = new_name.capitalize()
        print("\nCurrent value is: ",row[2])
        new_phone = 0
        try:
            new_phone = float(input("Please enter 0 to retain value or enter new phone:  "))
        except Exception as e:
            print(f"\nInvalid input: phone number retained")
            a = 1
        if new_name == "":
            new_name = row[1] 
        if new_phone == 0:
            new_phone = row[2]
        sql = "UPDATE couriers set courier_name = %s, courier_phone = %s where courier_id = %s"
        val = (new_name, new_phone, c_index)
        try:
            cursor.execute(sql, val)
            connection.commit()
        except Exception as e:
            print(f"\n {e}") 
            a = 1   
    cursor.close()
    connection.close()
    if a == 0:
        print('\Courier successfully updated') 

def delete_courier_d():
    a = 0 
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
    #########################################################
    cursor.execute('SELECT courier_id, courier_name, courier_phone FROM couriers')
    rows = cursor.fetchall()
    print("\n{:<1} {:<15} {:<20} {:<10}".format("","Courier Id","Courier Name","Courier Phone"))
    for row in rows:
        print("{:<1} {:<15} {:<20} {:<10}".format("",row[0],row[1],row[2]))
    while True:
        try:
            c_index = int(input("\nPlease enter Courier Id to delete: "))
            sql = "SELECT courier_id FROM couriers where courier_id = %s"
            cursor.execute(sql, c_index)            
            rows = cursor.fetchall() 
            if len(rows) == 0:
                print("Courier does not exists") 
            else:              
                break
        except Exception as e:
            print(f'{e},\nInvalid input')
    confirm = input("Are you sure? Y/N:   ")
    if confirm.capitalize() == 'Y':
        sql = "DELETE from couriers where courier_id = %s"
        val = (c_index)
    #########################################################
        try:
            cursor.execute(sql, val)
            connection.commit()
            print("\nCourier successfully deleted")
        except Exception as e:
            print(e)
    elif confirm.capitalize() == 'N':
        print("\nCourier not deleted")
    else:
        print("\nInvalid choice")    
    cursor.close()
    connection.close()    
    