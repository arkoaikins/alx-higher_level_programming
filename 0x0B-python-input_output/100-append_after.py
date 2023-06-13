#!/usr/bin/python3
"""
a function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after -  inserts a line of text to a file, after each line
                    containing a specific string

    args - filename="":file to insert line of text into
           search_string="": The string to search for in the text
           new_string="": the string to add the file

    """

    with open(filename, 'r', encoding='UTF-8') as my_file:
        text_list = []
        while True:
            text = my_file.readline()
            if text == "":
                break
            text_list.append(text)
            if search_string in text:
                text_list.append(new_string)
    with open(filename, 'w', encoding='UTF-8') as my_file:
        my_file.writelines(text_list)
