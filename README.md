# Purchase-Analytics Solution by Samuel D. Judge

## Table of Contents
1. [Problem](README.md#problem)
1. [Basic Strategy](README.md#basic-strategy)
1. [Assumptions](README.md#assumptions)
1. [Functions in Program](README.md#functions-in-program)
1. [Contact Information](README.md#contact-information)

## Problem

Instacart has published a [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders.

*I was told to calculate, for each department, the number of times a product was requested, number of times a product was requested for the first time, and a ratio of those two numbers.*


## Basic Strategy
The general idea behind this program was fairly simple. We had essentially two data sets, each of which contained two important pieces of data. The first was all the products where the important information was the unique product id number and the other was the department where that product was stored. The second data set contained all orders and the important information therein was what product was ordered and whether or not it was a reordered item by the customer. 
My technique was to first run through the products data set and create two dictionaries. The first dictionary contained keys that were the product ID and the associated element was its department number. I did this by noticing that the product ID was the first element and the department number was the last once I split by commas. The second dictionary was keyed by department numbers and its associated element was a list [0,0,0].
Once these dictionaries existed, I ran through the orders. Every time I came across an order, I checked it with the products dictionary by key. If such a product existed, the department was returned and I went to the department dictionary. Within that dictionary, I keyed in the department number and then changed the list accordingly: I always added one to the first element. If the order was a first time order, I added one to the second element as well. Then the third element was calcuated simply by taking the ratio of the second to the first. 

## Assumptions
* There is an assumption that the data matches the form that was told to us in the project repo. However, there are checks for this throughout the code. 
* This program is also using sys library. It only uses it in one place: when the function is called at the very end in order to be run from the run.sh. The programs themselves should work without or without it. 
* Keeping in line with statement above, the very first line of code imports this library. 


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
