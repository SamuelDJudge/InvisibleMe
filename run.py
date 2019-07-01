import time
import datetime
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext,SparkSession,Row

from user_input import *
from encryption import *
from decryption import *
from creating_keys import *
from column_operations import *

#x = u'C00128876|N|Q1|P|25020162899|15||CONNELLY, PAT|MANHATTAN|KS|66503||ICE CORPORATION|02072005|250||||||2042920051056611647'
#print(cleaning_data(x,key_dict,column_list))
#key = 'jeo44do44ehggcoc'
#init_vector = '89p2lq4uoqc88ots'
#print(str(encryption("CONNELLY, PAT",key,init_vector)))






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


