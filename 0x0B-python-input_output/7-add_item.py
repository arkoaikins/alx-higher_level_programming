#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save
them to a file

"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


""" an empty python list"""
my_list = []

"""
take command line arguments
"""
arguments = sys.argv[1:]

"""
cheking for JSON file
"""
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

my_list.extend(arguments)

save_to_json_file(my_list, "add_item.json")
