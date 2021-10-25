import csv
from logging import exception
import os
from os import system
from types import new_class
from typing import DefaultDict, List, Dict, Sequence
from dotenv import load_dotenv
import pymysql

def create_product(p_dict:list):
    product_name=input("Enter a new product:")
    product_price=(input("Enter product price:"))
    product_name=product_name.strip()
    product_price=product_price.strip()
    latest_prod= {"product_name": product_name,"product_price": float(product_price)}
    p_dict.append(latest_prod)
    #return latest_prod

def update_product(p_dict:list):
        print_prod(p_dict)
        p_index = int(input("\nPlease enter product index to update: "))
        if p_index in range(0,len(p_dict)+1):
            print("\nCurrent value is:",p_dict[p_index-1]["product_name"])
            new_name = input("Please press enter to retain value or enter new name: ")
            print("\nCurrent value is: ",p_dict[p_index-1]["product_price"])
            new_price = 0
            try:
                new_price = float(input("Please enter 0 to retain value or enter new price: "))
            except Exception as e:
                print("\nInvalid input")
            if new_name != "":
                p_dict[p_index-1]["product_name"] = new_name
            if new_price != 0:
                p_dict[p_index-1]["product_price"] = new_price
            print("\n-----------Updated list of orders-----------\n")     
            print_prod(p_dict) 
        else:
            print("invalid choice")
            
def del_product(p_dict:list):
    print_prod(p_dict)
    p_index=int(input("\nEnter product index to delete: ")) 
    print(p_dict[p_index-1]["product_name"]," deleted")
    del p_dict[p_index-1]     
    print("\n-----------Updated list of orders-----------\n") 
    print_prod(p_dict)        

def create_courier(c_dict:list):
    courier_name=input("Enter a new courier:")
    courier_number=(input("Enter phone number:"))
    courier_name=courier_name.strip()
    courier_number=courier_number.strip()
    latest_courier= {"courier_name": courier_name,"courier_number": courier_number}
    c_dict.append(latest_courier)   

def update_courier(c_dict:list):
        print_courier(c_dict)
        c_index = int(input("\nPlease enter courier index to update: "))
        if c_index in range(0,len(c_dict)+1):
            print("\nCurrent value is: ",c_dict[c_index-1]["courier_name"])
            new_name = input("Please press enter to retain value or enter new name: ")
            print("\nCurrent value is: ",c_dict[c_index-1]["courier_number"])
            new_number = 0
            try:
                new_number = int(input("Please enter 0 to retain value or enter new number: "))
            except Exception as e:
                print("\nInvalid input")
            if new_name != "":
                c_dict[c_index-1]["courier_name"] = new_name
            if new_number != 0:
                c_dict[c_index-1]["courier_number"] = new_number
            print_courier(c_dict) 
        else:
            print("\nInvalid choice")

def del_courier(c_dict:list):
    print_courier(c_dict)
    c_index=int(input("\nEnter courier index to delete: ")) 
    print(c_dict[c_index-1]["courier_name"]," deleted")
    del c_dict[c_index-1]
    #print('\n')
    print("\n-----------Updated list of orders-----------\n")     
    print_courier(c_dict)
            
def create_order(o_dict:list,couriers:list,products:list):
    customer_name=input("Enter Customer name:")
    customer_address=(input("Enter Customer address:"))
    customer_phone= (input("Enter Customer phone:"))
    order_status ="Preparing"
    customer_name=customer_name.strip()
    customer_address = customer_address.strip()
    customer_phone = customer_phone.strip()
    order_status = order_status.strip()
    print("Courier list:")
    print_courier(couriers)
    courier_index = input("\nPlease enter courier index to add a courier to the order:")
    print("Product list:")
    print_prod(products)
    product_index=[]
    product_index = input("\nPlease enter comma seperated product index to add products to the order:")
    latest_order= {
                    "customer_name": customer_name,
                    "customer_address": customer_address,
                    "customer_phone":customer_phone,
                    "order_status":order_status,
                    "courier": courier_index,
                    "products": product_index
                }
    print("Order created, status - Preparing")
    o_dict.append(latest_order)

def update_order_status(o_dict:list):
    order_status = ['Preparing','Ready','Out For Delivery','Delivered','Cancelled']
    print_order(o_dict)
    o_index = int(input("\nPlease enter order index to update status: "))
    if o_index in range(0,len(o_dict)+1):
        print("\nCurrent status is: ",o_dict[o_index-1]["order_status"])
        for (i,item) in enumerate(order_status, start =1):
            print(i,item)
        new_order_status = 0    
        new_order_status = int(input("Please enter 0 to retain value or enter the number for new status: "))
        print(new_order_status)
        if new_order_status != 0:
            #print(order_status[new_order_status])
            o_dict[o_index-1]["order_status"] = order_status[new_order_status-1]
        print("\n-----------Updated list of orders-----------\n") 
        print_order(o_dict) 
    else:
        print("\nInvalid choice")

def update_order(o_dict:list,c_dict:list,p_dict:list):
    print_order(o_dict)
    o_index = int(input("\nPlease enter order index to update: "))
    if o_index in range(0,len(o_dict)+1):
        new_choice = int(input('''
        \nPlease enter the field index to update:
        ------------------------------
        1 Customer Name
        2 Customer Address
        3 Customer Phone Number
        4 Courier 
        5 Products 
        ------------------------------
        '''))
        if new_choice in range(1,6):
            if new_choice == 1:
                print("\nCurrent value is: ",o_dict[o_index-1]["customer_name"])
                new_value = input("\nPlease enter new name: ")
                o_dict[o_index-1]["customer_name"] = new_value
            if new_choice == 2:
                print("\nCurrent value is: ",o_dict[o_index-1]["customer_address"])
                new_value = input("\nPlease enter new address: ")
                o_dict[o_index-1]["customer_address"] = new_value                
            if new_choice == 3:
                print("\nCurrent value is: ",o_dict[o_index-1]["customer_phone"])
                new_value = input("\nPlease enter new phone number: ")
                o_dict[o_index-1]["customer_phone"] = new_value                
            if new_choice == 4:
                #print(c_dict[int(o_dict[o_index-1]["courier"])-1]["courier_name"])
                print("\nCurrent value is: ",c_dict[int(o_dict[o_index-1]["courier"])-1]["courier_name"])
                print("\n--------------------------------")
                print_courier(c_dict)
                new_value = input("Please enter new courier from the above list: ")                
                o_dict[o_index-1]["courier"] = new_value                
            if new_choice == 5:
                print("\nCurrent value is: ",o_dict[o_index-1]["products"])  
                print("--------------------------------\n") 
                print_prod(p_dict)
                new_value = input("Please enter comma seperated product index to add products to the order: ")
                o_dict[o_index-1]["products"] = new_value                                                                           
        print("\n-----------Updated list of orders-----------\n") 
        print_order(o_dict) 
    else:
        print("invalid choice")            

def del_order(o_dict:list):
    print_order(o_dict)
    o_index=int(input("\nEnter order index to delete: "))
    #y_n=input("Are you sure you want to delete the order? Y/N: ")
    #print(y_n)
    #if y_n == 'Y' or 'y':
    print("\nOrder for customer ",o_dict[o_index-1]["customer_name"]," deleted")
    del o_dict[o_index-1]
    print("\n-----------Updated list of orders-----------\n")      
    print_order(o_dict)
    #elif y_n == 'N' or 'n':
    #    print("Order not deleted")
    #else:
    #    print("Invalid input")        
    
def load_dict(filename:str):
    my_dict =[]
    if os.path.isfile(filename) and os.stat(filename).st_size != 0:
        with open(filename,'r') as csv_file:             
            reader = csv.DictReader(open(filename))
            my_dict = list(reader)
    return my_dict

def print_prod(my_dict:list):
    #clear_screen()
    print("\n{:<5} {:<8} {:<20} {:<10}".format("","Index","Product Name","Product Price"))
    j=0
    for i in my_dict:
        j=j+1
        print("{:<5} {:<8} {:<20} {:<10}".format("",j, i["product_name"],i["product_price"]))  

def print_courier(my_dict:list):
    #clear_screen()
    print("\n{:<5} {:<8} {:<15} {:<10}".format("","Index","Courier Name","Courier Phone Number"))
    j=0
    for i in my_dict:
        j=j+1
        print("{:<5} {:<8} {:<15} {:<10}".format("",j, i["courier_name"],i["courier_number"]))  

def print_order(my_dict:list):
    #clear_screen()
    print("\n{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("","Index","Customer name","Customer Address","Phone Number","Order Status", "Courier", "Product"))
    j=0
    for i in my_dict:
        j=j+1
        #print(i)
        print("{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("",j, i["customer_name"],
                                                            i["customer_address"],
                                                            i["customer_phone"],
                                                            i["order_status"],
                                                            i["courier"],
                                                            i["products"])
        )  
                                        
def save_dict(items: list, filename:str):   
    if len(items) != 0:
        try:    
            with open(filename,'w',newline='') as file:
                fieldnames = items[0].keys()
                writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter = ',')
                writer.writeheader()
                for item in items:
                    writer.writerow(item)  
        except Exception as e:
            print(f'An error has occured in module {items} - {e}')       
#open file and overwrite the contents       

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
    cursor.execute('SELECT product_id, product_name, product_price FROM products')
    rows = cursor.fetchall()
    print("\n{:<1} {:<15} {:<20} {:<10}".format("","Product_Id","Product Name","Product Price"))
    for row in rows:
        print(f'   {row[0]}               {row[1]}                     {row[2]}')
        #print(f'Product_Id: {row[0]}, Product_Name: {str(row[1])}, Product_Price: {float(row[2])}')
    cursor.close()
    connection.close()

def create_product_d():
    product_name=input("Enter a new product:")
    product_price=(input("Enter product price:"))
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
    except ValueError as e:
        print(e)
    connection.commit()
    cursor.close()
    connection.close()

def update_product_d():
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
        print(f'   {row[0]}               {row[1]}                     {row[2]}')
    try:
        p_index = int(input("\nPlease enter product_id to update: "))
    except exception as e:
        print("\nInvalid input")
    sql = "SELECT product_id, product_name, product_price FROM products where product_id = %s"
    val = (p_index)
    cursor.execute(sql, val)
    row = cursor.fetchone()
    if row == None:
            print("\nInvalid input")
    else:        
        print("\nCurrent value is:",row[1])
        new_name = input("Please press enter to retain value or enter new name: ")
        print("\nCurrent value is: ",row[2])
        new_price = 0
        try:
            new_price = float(input("Please enter 0 to retain value or enter new price: "))
        except Exception as e:
            print("\nInvalid input")
            a = 1
        if new_name == "":
            new_name = row[1] 
        if new_price == 0:
            new_price = row[2]
        print(new_name,new_price)
        sql = "UPDATE products set product_name = %s, product_price = %s where product_id = %s"
        val = (new_name, new_price, p_index)
    #########################################################
    try:
        cursor.execute(sql, val)
    except exception as e:
        print(e)
    connection.commit()
    cursor.close()
    connection.close()
    if a != 1:
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
    print("\n{:<1} {:<15} {:<20} {:<10}".format("","Product_Id","Product Name","Product Price"))
    for row in rows:
        print(f'   {row[0]}               {row[1]}                     {row[2]}')
    while True:
        try:
            p_index = int(input("\nPlease enter product_id to delete: "))
            break
        except exception as e:
            print(f'{e},\nInvalid input')
    confirm = str(input("Are you sure? Y/N:   "))
    if confirm == 'Y' or 'y':
        print(confirm)
        sql = "DELETE from products where product_id = %s"
        val = (p_index)
    #########################################################
        try:
            cursor.execute(sql, val)
            print("\nProduct successfully deleted")
        except exception as e:
            print(e)
    if confirm == 'N' or 'n':
        print(confirm)
        print("Product not deleted")         
    connection.commit()
    cursor.close()
    connection.close()

def print_grp_order(my_dict:list):
    #clear_screen()
    print("\nOrders By Order Status - Preparing: ")
    print("\n{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("","Index","Customer name","Customer Address","Phone Number","Order Status", "Courier", "Product"))
    j=0
    for i in my_dict:
        if i["order_status"] == "Preparing":
           j=j+1 
           print("{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("",j, i["customer_name"],
                                                               i["customer_address"],
                                                               i["customer_phone"],
                                                               i["order_status"],
                                                               i["courier"],
                                                               i["products"])
           )
    print("\nOrders By Order Status - Ready: ")
    print("\n{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("","Index","Customer name","Customer Address","Phone Number","Order Status", "Courier", "Product"))
    j=0
    for i in my_dict:
        if i["order_status"] == "Ready":
           j=j+1 
           print("{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("",j, i["customer_name"],
                                                               i["customer_address"],
                                                               i["customer_phone"],
                                                               i["order_status"],
                                                               i["courier"],
                                                               i["products"])
           )
    print("\nOrders By Order Status - Out For Delivery: ")
    print("\n{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("","Index","Customer name","Customer Address","Phone Number","Order Status", "Courier", "Product"))
    j=0
    for i in my_dict:
        if i["order_status"] == "Out For Delivery":
           j=j+1 
           print("{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("",j, i["customer_name"],
                                                               i["customer_address"],
                                                               i["customer_phone"],
                                                               i["order_status"],
                                                               i["courier"],
                                                               i["products"])
           )
    print("\nOrders By Order Status - Delivered: ")
    print("\n{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("","Index","Customer name","Customer Address","Phone Number","Order Status", "Courier", "Product"))
    j=0
    for i in my_dict:
        if i["order_status"] == "Delivered":
           j=j+1 
           print("{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("",j, i["customer_name"],
                                                               i["customer_address"],
                                                               i["customer_phone"],
                                                               i["order_status"],
                                                               i["courier"],
                                                               i["products"])
           )
    print("\nOrders By Order Status - Cancelled: ")
    print("\n{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("","Index","Customer name","Customer Address","Phone Number","Order Status", "Courier", "Product"))
    j=0
    for i in my_dict:
        if i["order_status"] == "Cancelled":
           j=j+1 
           print("{:<3} {:<8} {:<20} {:<25} {:<15} {:<20} {:<10} {:<5}".format("",j, i["customer_name"],
                                                               i["customer_address"],
                                                               i["customer_phone"],
                                                               i["order_status"],
                                                               i["courier"],
                                                               i["products"])
           )                                                       

def print_order_grp(my_dict:list):
    order_sts = set()    
    for i in my_dict:
        order_sts.add(i["order_status"])
    print(order_sts)    

        # print("\nOrders By Order Status - {order_sts[j]}: ")
"""     print(my_dict[0])
    print(my_dict[0].keys())
    print(my_dict[0].values())
    print(my_dict[0].items())
    for val,k in my_dict[0].items():
        print(val,k) """
     








# def load_env_var_d(a:int):
#         # Load environment variables from .env file
#         load_dotenv()
#         host = os.environ.get("mysql_host")
#         user = os.environ.get("mysql_user")
#         password = os.environ.get("mysql_pass")
#         database = os.environ.get("mysql_db")
#         # Establish a database connection
#         connection = pymysql.connect(
#             host,
#             user,
#             password,
#             database
#         )
#         cursor = connection.cursor()
#         cursor.close()
#         connection.close()
    
#if __name__ == '__main__':
                    
    #Load data from CSV files into Dictionary
    #prod = load_dict('products.csv')
    #courier = load_dict('couriers.csv')
    #order = load_dict('orders.csv')

    # Print data for testing
    #print(prod)
    #print(prod.items())
    #print(prod.keys())
    #print(prod.values())

    #print(courier)
    #print(courier.items())
    #print(courier.keys())
    #print(courier.values())

    #Create Product
    #prod = createProduct(prod)
    #print(prod)

    #Create Courier
    #courier = createCourier(courier)
    #print(courier)

    #Create Orders
    #orders = createOrder(order)
    #print(orders)

    #Save data in Dictionary into CSV file         
    #save_dict(prod,'products.csv')
    #save_dict(courier,'couriers.csv')
    #saveDict(orders,'orders.csv')
