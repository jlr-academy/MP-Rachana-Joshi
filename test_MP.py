#from unittest import mock
from types import new_class
from unittest.mock import patch, Mock
#from Sourcecode.dict_Functions_MP import update_order_status
from menu_MP import main_menu
import menu_MP
import dict_Functions_MP
import os
import csv
import pytest

# test_order = [{
#     "customer_name": "Ollie",
#     "customer_address": "Abbey Road",
#     "customer_phone": "0999999999",
#     "order_status": "Preparing",
#     "courier": 1,
#     "products": 1
# }]
# @patch("builtins.print")
# @patch("builtins.input")
# def test_menu_option_0(mock_input: Mock, mock_print: Mock):
# #assemble
#     new_dict = {"product_name":"Apple", "product price": "100"}
#     mock_input.side_effect = ["0"]
# #act
#     my_dict = {}
#     menu_MP.main_menu(new_dict)
#     #dict_Functions_MP.saveDict(new_dict,"products.csv")
#     if os.path.isfile("products.csv") and os.stat("products.csv").st_size != 0:
#         with open("products.csv") as csv_file:             
#             reader = csv.reader(csv_file)
#             my_dict = dict(reader)            
# #assert
#     assert my_dict == new_dict 
    
# @patch("builtins.input")    
# def test_create_product(mock_input:Mock):
#     #assemble
#     products = []
#     #latest_prod = ["product_name","product_price"]
#     expected = [{"product_name": "Cereal","product_price": float(2.29)}]
#     mock_input.side_effect = ["Cereal","2.29"]
#     #act
#     result = dict_Functions_MP.create_product(products)
#     #assert
#     assert result == expected
    
# @patch("builtins.input")
# def test_update_order_status(mock_input:Mock):
#     #assemble
#     mock_input.side_effect = ["4","4"]
#     expected = "Preparing"
#     #act
#     new_list = dict_Functions_MP.update_order_status(test_order)
#     result = new_list.get('order_status')
#     #assert
#     assert result == expected
    
######passes#######
@patch("builtins.input", side_effect=["0", "1"])
def test_main_menu_option_0(mock_input):
    # assemble
    #nothing to assemble  
    # act and assert
    with pytest.raises(SystemExit):
        menu_MP.main_menu()    
        
#@patch("builtins.print")        