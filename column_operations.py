from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext,SparkSession,Row

def cleaning_data(input_row):
    if en_or_de.lower() == "encryption":
        split_row = input_row.split(delimiter)
    elif en_or_de.lower() == "decryption":
        split_row = input_row.split(',')
    for a_column in column_list:
        key = key_dict[a_column][0]
        init_vector = key_dict[a_column][1]
        column_index = a_column - 1
        if en_or_de.lower() == "encryption":
            try:
                split_row[column_index] = str(encryption(split_row[column_index],key,init_vector))
            except:
                split_row[column_index] = "INVAID ENTRY"
        elif en_or_de.lower() == "decryption":
            try:
                split_row[column_index] = str(decryption(split_row[column_index],key,init_vector))
            except:
                split_row[column_index] = "INVAID ENTRY"
        else:
            raise ValueError("You should have inputted 'encryption' or 'decryption' as your option")            
    return Row(name = split_row[column_list[0]-1], zip_code = split_row[column_list[1]-1])

