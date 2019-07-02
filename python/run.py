# Imports
import time
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext,SparkSession

from creating_keys import *
from column_operations import *

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



# Timer
initial_time = time.time()

# Spark Initializing
conf = SparkConf().setAppName("First Attempt")
conf = conf.setMaster("local[*]")
sc   = SparkContext(conf = conf)
spark = SparkSession(sc)

if True:
# Spark Encryption
    initial_file = sc.textFile(file_path).map(cleaning_data)
    data_frame = initial_file.toDF()
    sql_context = SQLContext(sc)
    data_frame.write.mode('overwrite').csv(write_path)
# Save the keys in the case of encryption
    if en_or_de.lower() == "encryption":
        keys = sc.parallelize(key_list)
        key_data_frame = keys.toDF()
        key_data_frame.coalesce(1).write.mode('overwrite').csv(keys_write_path)

# End Timer
final_time = time.time()-initial_time
print("####################### PROGRAM COMPLETED IN "+str(final_time)+" SECONDS#######################")
