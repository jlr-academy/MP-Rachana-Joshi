from os import system
from typing import List
import dict_Functions_MP
import db_Functions
import csv
import pymysql
import exporttocsv

products =[]
couriers = []
orders =[]

def main_menu():
    dict_Functions_MP.clear_screen()
    menu = input('''
        Please enter your choice:
        -------------------------
        0 Save & Exit
        1 Product Menu
        2 Courier Menu
        3 Orders Menu
        -------------------------
        ''')
    if menu == ' ':
        dict_Functions_MP.clear_screen()
        exporttocsv.export_products_to_csv_d()
        exporttocsv.export_couriers_to_csv_d()
        #dict_Functions_MP.save_dict(products,"products.csv")
        #dict_Functions_MP.save_dict(couriers,"couriers.csv")
        dict_Functions_MP.save_dict(orders,"orders.csv")
        print("\nData saved. Thanks for visiting, bye!\n")
        exit()   
    if menu == '0':
        dict_Functions_MP.clear_screen()
        exporttocsv.export_products_to_csv_d()
        exporttocsv.export_couriers_to_csv_d()
        #dict_Functions_MP.save_dict(products,"products.csv")
        #dict_Functions_MP.save_dict(couriers,"couriers.csv")
        dict_Functions_MP.save_dict(orders,"orders.csv")
        print("\nData saved. Thanks for visiting, bye!\n")
        exit()    
    elif menu == '1':
        dict_Functions_MP.clear_screen()
        ask_choice_prod()
    elif menu == '2':
        dict_Functions_MP.clear_screen()
        ask_choice_courier()
    elif menu == '3':
        dict_Functions_MP.clear_screen()
        ask_choice_order()    
    else:
        print("********** Incorrect choice, please enter choice between 0 - 3 **********")
        main_menu()            
#Function to ask choice from the user for product menu
def ask_choice_prod():
    dict_Functions_MP.clear_screen()
    print("\n********** Product Menu **********\n")
    prod =input('''
        Enter your choice:
            ------------------------------
            0 Main Menu
            1 Print product list
            2 Create a new product
            3 Update an existing product
            4 Delete an existing product 
            ------------------------------
            ''')
    if prod == ' ':
        dict_Functions_MP.clear_screen()
        exporttocsv.export_products_to_csv_d()
        exporttocsv.export_couriers_to_csv_d()
        #dict_Functions_MP.save_dict(products,"products.csv")
        #dict_Functions_MP.save_dict(couriers,"couriers.csv")
        dict_Functions_MP.save_dict(orders,"orders.csv")
        print("\nData saved. Thanks for visiting, bye!")
        exit()     
    if prod == '0':
        main_menu()
    if prod == '1':
        dict_Functions_MP.clear_screen()
        #dict_Functions_MP.print_prod(products)
        db_Functions.print_products_d()
        input("\nPlease press any key to continue...")
        ask_choice_prod()
    if prod == '2':
        dict_Functions_MP.clear_screen()
        db_Functions.create_product_d()
        #dict_Functions_MP.create_product(products)
        input("\nPlease press any key to continue...")
        ask_choice_prod()
    if prod == '3':
        dict_Functions_MP.clear_screen()
        db_Functions.update_product_d()
        #dict_Functions_MP.update_product(products)
        input("\nPlease press any key to continue...")
        ask_choice_prod()
    if prod == '4':
        dict_Functions_MP.clear_screen()
        db_Functions.delete_product_d()
        #dict_Functions_MP.del_product(products)
        input("\nPlease press any key to continue...")  
        ask_choice_prod() 
    else:
        print("********** Incorrect choice, please enter choice between 0 - 4 **********")
        ask_choice_prod()        

#Function to ask choice from the user for courier menu
def ask_choice_courier():
    dict_Functions_MP.clear_screen()
    print("\n********** Courier Menu **********\n")
    courier =input('''
        Enter your choice:
            ------------------------------
            0 Main Menu
            1 Print courier list
            2 Create a new courier
            3 Update an existing courier
            4 Delete an existing courier 
            ------------------------------
            ''')
    if courier == ' ':
        dict_Functions_MP.clear_screen()
        exporttocsv.export_products_to_csv_d()
        exporttocsv.export_couriers_to_csv_d()
        #dict_Functions_MP.save_dict(products,"products.csv")
        #dict_Functions_MP.save_dict(couriers,"couriers.csv")
        dict_Functions_MP.save_dict(orders,"orders.csv")
        print("\nData saved. Thanks for visiting, bye!")
        exit()     
    if courier == '0':
        main_menu()
    if courier == '1':
        dict_Functions_MP.clear_screen()
        #dict_Functions_MP.print_courier(couriers)
        db_Functions.print_courier_d()
        input("\nPlease press any key to continue...")
        ask_choice_courier()
    if courier == '2':
        dict_Functions_MP.clear_screen()
        #dict_Functions_MP.create_courier(couriers)
        db_Functions.create_courier_d()
        input("\nPlease press any key to continue...")
        ask_choice_courier()
    if courier == '3':
        dict_Functions_MP.clear_screen()
        #dict_Functions_MP.update_courier(couriers)
        db_Functions.update_courier_d()
        input("\nPlease press any key to continue...")
        ask_choice_courier()
    if courier == '4':
        dict_Functions_MP.clear_screen()
        #dict_Functions_MP.del_courier(couriers)
        db_Functions.delete_courier_d()
        input("\nPlease press any key to continue...")  
        ask_choice_courier() 
    else:
        print("********** Incorrect choice, please enter choice between 0 - 4 **********")
        ask_choice_courier()

#Function to ask choice from the user for order menu        
def ask_choice_order():
    dict_Functions_MP.clear_screen()
    print("\n********** Order Menu **********\n")
    order =input('''
    Enter your choice:
        ------------------------------
        0 Main Menu
        1 Print orders list
        2 Create a new order
        3 Update an existing order status
        4 Update an existing order 
        5 Delete an existing order 
        ------------------------------
        ''')
    if order == ' ':
        dict_Functions_MP.clear_screen()
        exporttocsv.export_products_to_csv_d()
        exporttocsv.export_couriers_to_csv_d()
        #dict_Functions_MP.save_dict(products,"products.csv")
        #dict_Functions_MP.save_dict(couriers,"couriers.csv")
        dict_Functions_MP.save_dict(orders,"orders.csv")
        print("\nFiles saved. Thanks for visiting, bye!")
        exit()     
    if order == '0':
        main_menu()
    if order == '1':
        dict_Functions_MP.clear_screen()
        dict_Functions_MP.print_order(orders)
        dict_Functions_MP.print_grp_order(orders)
        #dict_Functions_MP.print_order_grp(orders)
        input("\nPlease press any key to continue...")
        ask_choice_order()
    if order == '2':
        dict_Functions_MP.clear_screen()
        dict_Functions_MP.create_order(orders,couriers,products)
        input("\nPlease press any key to continue...")
        ask_choice_order()
    if order == '3':
        dict_Functions_MP.clear_screen()
        dict_Functions_MP.update_order_status(orders)
        input("\nPlease press any key to continue...")
        ask_choice_order()
    if order == '4':
        dict_Functions_MP.clear_screen()
        dict_Functions_MP.update_order(orders,couriers,products)
        input("\nPlease press any key to continue...")  
        ask_choice_order()
    if order == '5':
        dict_Functions_MP.clear_screen()
        dict_Functions_MP.del_order(orders)
        input("\nPlease press any key to continue...")  
        ask_choice_order()     
    else:
        print("********** Incorrect choice, please enter choice between 0 - 4 **********")
        ask_choice_order()   
        
#load all files into theor respective lists.
# If the files do not exist or are empty, then lists ar empty
if __name__ == '__main__':
    #products = dict_Functions_MP.load_dict("products.csv")
    #couriers = dict_Functions_MP.load_dict("couriers.csv")
    #cursor = dict_Functions_MP.load_env_var_d(0)
    orders = dict_Functions_MP.load_dict("orders.csv")
    main_menu()
