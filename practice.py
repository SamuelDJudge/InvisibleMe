############################# IMPORTS ##########################################
#import random
#from Crypto.Cipher import AES
#import base64
import time
import datetime
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext,SparkSession,Row
#import boto3
#import botocore
###################################################################################






############################# ENCYRPTION ##########################################
def making_multiple_16(text):
    len_of_text = len(text)
    while len_of_text % 16 != 0:
        text += " "
        len_of_text = len(text)
    return text

def encryption(text,key,init_vector):
    coder = AES.new(key,AES.MODE_CBC,init_vector)
    code = coder.encrypt(making_multiple_16(text))
    code_64 = str(base64.b64encode(code))
    return code_64
###################################################################################







############################# DECYRPTION ##########################################
def decryption(coded_64_message,key,init_vector):
    byte_object = base64.b64decode(coded_64_message+"===")
    decoder = AES.new(key,AES.MODE_CBC,init_vector)
    return decoder.decrypt(byte_object).decode('utf-8').strip()
###################################################################################









############################# NEW FILE NAME ##########################################
def finding_location(file_path):
        delimiter = file_path[-1]
        while delimiter != "/":
                file_path = file_path[:-1]
                delimiter = file_path[-1]
        return file_path
###################################################################################







############################# USER INPUT ##########################################
column_list=[1,2]
file_path = "s3a://fecpoliticaldata/itcont_2006.txt"
write_path = "s3a://fecdatakeys/encrypted"
read_path = "s3://fecdatakeys/encrypted/part-00000-8def0398-3961-4a1d-9f0b-2e830ac84039-c000.csv"
delimiter = '|'
en_or_de = "decryption"
id_num = "part-00000-ab4cde60-93c1-4bdb-89d9-835cc498047f-c000"
###################################################################################








########################### KEY LOCATION #######################################
keys_write_path = "s3a://fecdatakeys/keys"
keys_read_path = "s3://fecdatakeys/keys/part-00000-f4922dc0-b219-4ffe-9833-e63f9ccc0316-c000.csv"
###################################################################################










########################### CREATING KEYS #######################################
qwerty_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

def creating_a_key(qwerty_list):
    key = ""
    for i in range(16):
        random_var = random.randint(0,len(qwerty_list)-1)
        key += qwerty_list[random_var]
    return key

def creating_dict_of_keys(columns):
    num_of_cols = len(columns)
    key_dict = {}
    for a_col in columns:
        key_dict[a_col] = [creating_a_key(qwerty_list),creating_a_key(qwerty_list)]
    return key_dict

def making_key_dict(en_or_de,column_List):

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
#################################################################################






########################### COLUMN OPERATIONS #######################################
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
                #split_row[column_index] = split_row[column_index]
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
#################################################################################




########################### TIMER #######################################
initial_time = time.time()
#################################################################################





########################### SPARK SETUP #######################################
conf = SparkConf().setAppName("First Attempt")
conf = conf.setMaster("local[*]")
sc   = SparkContext(conf = conf)
spark = SparkSession(sc)
#################################################################################












########################### SPARK ENCRYPTION #######################################
if en_or_de.lower() == "encryption":
    keys = sc.parallelize(key_list)
    initial_file = sc.textFile(file_path).map(cleaning_data)
    data_frame = initial_file.toDF()
    key_data_frame = keys.toDF()
    sql_context = SQLContext(sc)
    data_frame.coalesce(1).write.mode('overwrite').csv(write_path)
    key_data_frame.coalesce(1).write.mode('overwrite').csv(keys_write_path)
#################################################################################











########################### SPARK DECRYPTION #######################################
if en_or_de.lower() == "decryption":
    initial_file = sc.textFile(read_path).map(cleaning_data)
    data_frame = initial_file.toDF()
    sql_context = SQLContext(sc)
    data_frame.coalesce(1).write.mode('overwrite').csv(write_path)
#################################################################################






########################### TIMER #######################################
final_time = time.time()-initial_time
print("####################### THIS TOOK "+str(final_time)+" SECONDS#######################")
#################################################################################
