# Invisible Me by Samuel D. Judge

## Table of Contents
1. [Problem](README.md#problem)
1. [Basic Strategy](README.md#basic-strategy)
1. [Assumptions](README.md#assumptions)
1. [Files in Repo](README.md#functions-in-program)
1. [Contact Information](README.md#contact-information)

## Problem

In the age of machine learning, the characteristics of an individual that can be used to personally identify them is constantly changing. Originally an individuals full name, social security number, and home address were considered "identifying." The list has since grown to include biometric information, IP address, devide ID, and even ones academic record. For an interesting perspective on how machine learning is changing this, watch this [video](https://www.youtube.com/watch?v=aircAruvnKk). As a result, many databases that have already been published online will need to be retroactively pulled and encrypted. While encryption is easy to handle on a line-by-line basis, recieving 5 billion lines that needs to be quickly and efficiently encrypted is not plausible for a normal computer system.

[dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders.

*Solution:* The goal of this program is to handle this problem of scale. It will use PySpark to distribute the processing of the file across several Amazon EC2 nodes before republishing the data back from whence it came. 


## Basic Strategy


## Assumptions
* I am assuming that the user is storing their information in an Amazon S3 bucket. 
* I am assuming that the information is relational and organized in a .csv type format, though the program does allow for flexibility as to what the delimiter is. 
* There are multiple requirements for technology, specified in the _requirements.txt_ file. 


## Functions in Program 

### creating_department_products_dictionary

#### input: 
*products_file_name* -- This should be a STRING and end with .csv. You simply need to key in the 'products.csv' (or otherwise named) file. Assuming that your .csv has product_id first and department_id last, this will work. 

#### description: 
This function was intended to create the dictionaries mentioned above. Throughout the code, they are called departments and products. It also counts the number of errors produced by reading the data file, though more descriptions of those can be found in the code itself as comments. 

### reordered_value

#### input: 
*value* -- This should be a STRING. The function expects a '0' or a '1' as a string (which in the data files indicates oredered v. not). It will return "False" if the former and "True" if the latter. This will return "Error" as a string if anything else is inputted.  

#### description: 
This simply tells us if we have a valid entry for reordered or not and then what that value is. We use the truth value in a if statement in the next function. 

### collecting_data

#### input: 
*products_file_name* and *orders_file_name* -- These should both be STRINGs and end with .csv. The products_file_name is the same as listed in the first function above. The *orders_file_name* is the list of all orders. Again, under the assumption that the order ID is listed second and the department ID is listed last, this will work. 

#### description: 
This will take in the two dictionaries created by the function **creating_department_products_dictionary**, run through all orders in the input order data, check it against the products dictionary, and then adjust the [a,b,c] list in the departments dictionary accordingly. It also checks for several different types of errors, though those can be seen as comments in the code. It will output the departments dictionary, with all data accounted for in those lists. 

### writing_to_new_file

#### input: 
*data_dictionary* and *report_file_name* -- These should both be STRINGs and end with .csv. The *data_dictionary* is what is produced by the function **collecting_data**, but this function will work for any dictionary that has associated elements [a,b,c] as a list. The report_file_name is simply whatever you intend for a name as a file name. 

#### description: 
This program uses writelines to write all the information to a .csv file (name of your choosing: i.e. report_file_name). It's intended purpose is to consolidate the information collected from the program **collecting_data**. 

### combining_functions

#### input: 
*products_file_name*,*orders_file_name*, and *report_file_name* -- These should all be STRINGs and end with .csv. Each of these are described above. 

#### description: 
This just consolidates and runs **collecting_data**(*products_file_name*,*orders_file_name*) and **writing_to_new_file**(*products_file_name*,*orders_file_name*, *report_file_name*) at the same time rather than having to enter them individually. 

## Contact Information
* Samuel David Judge
* Samuel.D.Judge@gmail.com
* 269.921.0330
