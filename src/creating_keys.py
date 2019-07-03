# Imports
import random
import boto3
import botocore
from user_input import *


qwerty_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

# Creating a random key
### This function randomly picks 16 characters from the QWERTY list specified above.
### Two of these will be used as the key and initial vector for AES

def creating_a_key(qwerty_list: list) -> str:
    key = ""
    for i in range(16):
        random_var = random.randint(0,len(qwerty_list)-1)
        key += qwerty_list[random_var]
    return key

# Creating a dictionary of random keys
### This function takes the columns to be encrypted and creates a dictionary with the following schema:
### column_name = [column_key, column_initial_vector]

def creating_dict_of_keys(columns: list) -> dict:
    num_of_cols = len(columns)
    key_dict = {}
    for a_col in columns:
        key_dict[a_col] = [creating_a_key(qwerty_list),creating_a_key(qwerty_list)]
    return key_dict

# Choosing the correct key dictionary based on encryption or decryption
### This function combines the previous function with the potential of DECRYPTING.
### Based on the user input, it creates the correct keys dictionary.

def making_key_dict(en_or_de: str,column_list: list) -> (dict,list):
    if en_or_de.lower() == "encryption":
        key_dict = creating_dict_of_keys(column_list)
        key_list = []
        for a_key in column_list:
            key_list.append([a_key, key_dict[a_key][0],key_dict[a_key][1]])

    elif en_or_de.lower() == "decryption":
        bucket_name = 'fecdatakeys'
        key = "keys/"+id_num+".csv"
        s3 = boto3.resource('s3')
        try:
            s3.Bucket(bucket_name).download_file(key, "keys_"+id_num+".csv")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("YOUR KEY DOES NOT EXIST")
            else:
                raise

        key_dict = {}
        keys = open("keys_"+id_num+".csv","r+")
        counter = 0
        for a_line in keys:
            key_dict[column_list[counter]] = [a_line[1],a_line[2]]
            counter += 1

    else:
        raise ValueError("You should have inputted 'encryption' or 'decryption' as your option")
    return key_dict, key_list

# Variables
### Universially naming the variables key_dict and key_list which will be used in "column_operations.py"
output = making_key_dict(en_or_de,column_list)
key_dict = output[0]
key_list = output[1]
