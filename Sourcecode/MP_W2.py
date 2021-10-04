import os
import time
# add some product names
Furniture = []
Courier = []
#print lists
        
    
def print_list(list):
    # try:
    #     with open("My_Products.txt","r") as prod_file:
    #         #prod_line = prod_file.readlines()
    #         Furniture.extend(prod_file.readlines())
    #         print("Here are the products:")
    # except Exception as e:
    #     print("Please see the error: " + str(e))
    for i in list:
        print(list.index(i)+1,f".", i)    
        

    
def create_product(list):
    new_product=input("Enter a new product: ")
    # ln_product = str.lower(new_product)
    # for k in range(len(Furniture)):
            #Furniture[k] = Furniture[k].lower()
        # if Furniture[k].lower() == ln_product:
        #     print("Product already exist")
        #     input("Please press any key to continue...")
        #     ask_choice_prod()
        # else:    
        #     if k+1 == len(Furniture):
    list.append(new_product)   
    print("Here is the new list of products added recently: ")
    print_list(list)  
    
def update_product(list):
    print("Current list of products:")
    print_list(list)
    old_prod = input("Which product do you want to update? ")
    update_prod = input("What would you like to update it to? ")
    if old_prod in list:
        for j in range(len(list)):
            itemname = list[j]
            if old_prod.lower() == itemname.lower():
                list[j] = update_prod
                print(f'{itemname} successfully updated to {update_prod}. Current list of products:')
                print_list(list)
                return
    # for j in range(len(Furniture)):
    #     if Furniture[j] == old_prod:
    #         Furniture[j] = update_prod
    #         print(Furniture)
    #     # return 1
    else:
        print("Product not found")
        return    
    #ask_choice_prod()
                
#     try:
#         with open("My_Products.txt","a") as prod_file:
#             prod_file.write(new_product)
#             print(f"Product successfully added")
#             p_prod()
#     except Exception as e:
#         print("Please see the error: " + str(e))
# #        time.sleep(5)
#         input("Please press any key to continue...")
    
def delete_product(list):
    print("Current list of products:")
    for k in list:
        print(list.index(k)+1,f".", k)
    del_prod = input("Which product do you want to delete? ")
        #j= 0 
    for z in range(len(list)):
        if list[z] == del_prod:
            confirm = input("Are you sure you want to delete the product? Y/N: ")
            if confirm == "Y" or "y":
                Furniture.pop(z)
                print("Product Deleted. Current list of products: ")
                print_list(list)
                return
            elif confirm =="N" or "n":
                print("You selected not to delete the product")
                return
            else:
                return
        else:
            print("Product not found")
            return
def list_to_file(list):
    file = open("Products.txt",'w')
    for product in list:
        file.write(product + '\n')
    file.close()       
#PRINT main menu options
def main_menu():
    os.system('cls')
    user_ip = int(input('''
        Please enter your choice: 
        -------------------------
        0 Exit App
        1 View Menu
        -------------------------
        '''))
    if user_ip == 0:
        print("********** Exiting, thanks you for visiting us **********")
        exit()
    elif user_ip == 1:
        os.system('cls')
        ask_submenu()    
    else:
        os.system('cls')
        print("********** Incorrect choice, please enter 0 or 1 **********")
        main_menu()        

#Function to check if user wants to choose product menu or courier menu
def ask_submenu():
    os.system('cls')
    submenu = int(input('''
        Please enter your choice:
        -------------------------
        0 Save & exit
        1 Product Menu
        2 Courier Menu
        3 Main Menu
        -------------------------
        '''))
    if submenu == 0:
        os.system('cls')
        print("Files Saved")
        list_to_file(Furniture)
        exit()    
    elif submenu == 1:
        os.system('cls')
        ask_choice_prod()
    elif submenu == 2:
        os.system('cls')
        ask_choice_courier()
    elif submenu == 3:
        os.system('cls')
        main_menu()    
    else:
        print("********** Incorrect choice, please enter choice between 0 - 3 **********")            
#Function to ask choice from the user for product menu
def ask_choice_prod():
    os.system('cls')
    print("********** Product Menu **********\n")
    prod =int(input('''
        Enter your choice:
        ------------------------------
        0 Main Menu
        1 Print product list
        2 Create a new product
        3 Update an existing product
        4 Delete an existing product 
        ------------------------------
        '''))
    if prod == 0:
        main_menu()
    if prod == 1:
        print_list(Furniture)
        input("Please press any key to continue...")
        ask_choice_prod()
    if prod == 2:
        create_product(Furniture)
        input("Please press any key to continue...")
        ask_choice_prod()
    if prod == 3:
        update_product(Furniture)
        input("Please press any key to continue...")
        ask_choice_prod()
    if prod == 4:
        delete_product(Furniture)
        input("Please press any key to continue...")  
        ask_choice_prod() 
    else:
        print("********** Incorrect choice, please enter choice between 0 - 4 **********")
        ask_choice_prod()        
        
            

#Function to ask choice from the user for courier menu
def ask_choice_courier():
    print("********** Courier Menu **********\n")
    ask_submenu()
   
main_menu()
