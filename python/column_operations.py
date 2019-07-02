# Imports
from pyspark.sql import Row

from encryption import *
from decryption import *
from creating_keys import key_dict
#from user_input import *

file = open("/home/ubuntu/InvisibleMe/python/system_info.csv","r+")
for a_line in file:
    a_line = a_line[:-2]
    a_line = a_line.split(',')
    column_list_str = a_line[4:]
    column_list = []
    for a_string in column_list_str:
        column_list.append(int(a_string))
    file_path = str(a_line[0])
    write_path = str(a_line[1])
    en_or_de = str(a_line[2])
    delimiter_list = ["period", "comma", "line", "tab", "newline"]
    delimiter_charaters = [".",",","|","\t","\n"]
    delimiter = delimiter_charaters[delimiter_list.index(str(a_line[3]))]
file.close()
print("##################", column_list,file_path,write_path,delimiter,"#################")



# Cleaning Data
### This function takes each line from the input file, checks to see if the column
### is one of the columns specified to be encrypted or decrypted, performs that operation
### and then returns a Row with schema:
### "i" = transformed row[i] or i = transformed row[i] based on whether the row was specified or not.

#def cleaning_data(input_row: list) -> Row:
def cleaning_data(input_row):
    row_dict = {}

    if en_or_de.lower() == "encryption":
        split_row = input_row.split(delimiter)
    elif en_or_de.lower() == "decryption":
        split_row = input_row.split(',')

    for column_index in range(len(split_row)):

        ### Checks to see if the column was one of the ones to be transformed...
        if column_index in column_list:
            a_column = split_row[column_index]
            if len(a_column) == 0:
            ### Making each element have non-zero length, without changing the meaning.
                a_column = "NULL"
            key = key_dict[column_index][0]
            init_vector = key_dict[column_index][1]

            if en_or_de.lower() == "encryption":
                try:
                    row_dict[str(column_index)] = str(encryption(a_column,key,init_vector))
                except:
                    row_dict[str(column_index)] = "INVALID ENTRY"

            elif en_or_de.lower() == "decryption":
                try:
                    row_dict[str(column_index)] = str(decryption(a_column,key,init_vector))
                except:
                    row_dict[str(column_index)] = "INVALID ENTRY"

            else:
                raise ValueError("You should have inputted 'encryption' or 'decryption' as your option")

        ### Otherwise, just returns the row back.
        else:
            row_dict[str(column_index)] = str(split_row[column_index])
    return Row(**row_dict)
