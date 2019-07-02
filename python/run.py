# Imports
import time
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext,SparkSession

from creating_keys import *
from column_operations import *




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
