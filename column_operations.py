from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext,SparkSession,Row

from user_input import *
from encryption import *
from decryption import *
from creating_keys import key_dict, key_list


def cleaning_data(input_row):
    row_dict = {}
    if en_or_de.lower() == "encryption":
        split_row = input_row.split(delimiter)
    elif en_or_de.lower() == "decryption":
        split_row = input_row.split(',')
    for column_index in range(len(split_row)):
        if column_index in column_list:
            a_column = split_row[column_index]
            if len(a_column) == 0:
                a_column = "NULL"
            key = key_dict[column_index][0]
            init_vector = key_dict[column_index][1]
            if en_or_de.lower() == "encryption":
#                try:
                row_dict[str(column_index)] = str(encryption(a_column,key,init_vector))
#                except:
#                    row_dict[str(column_index)] = "INVALID ENTRY"
            elif en_or_de.lower() == "decryption":
                try:
                    row_dict[str(column_index)] = str(decryption(a_column,key,init_vector))
                except:
                    row_dict[str(column_index)] = "INVALID ENTRY"
            else:
                raise ValueError("You should have inputted 'encryption' or 'decryption' as your option")
        else:
            row_dict[str(column_index)] = str(split_row[column_index])
    return Row(**row_dict)

