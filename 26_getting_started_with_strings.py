# this is the place where you import all module files in python 
import math
# this is the place where you write all your funcition defination and global variable 

# this is the place where you write your @main() funtion code

'''Getting started with python strings '''

'''NOTE : There are no data-types in python, first they all the data types we are using are the 
           objects of particular class which comes with its own built-in-functions and methods
           basically functions which are associated with class defination and its objects are 
           reffered as 'methods'
'''

message = "this is just a simple message!!!"

'''By defination string is sequence of charcaters or an array of characters stored in continous memory'''
'''Note computer do not deals woth charcaters the only langauge computer understands is binary lang '''
'''All the sentences, words and charaters you see on screen are internally stored and manupulated as a
   combination of 0s and 1s '''

'''
The conversion of characters to a number is called encoding 
The conversion of number to characters is called decoding 
ASCII and Unicode are some popular encoding
'''

print(type(message))
'''The above print statement will print the class it belongs to  '''

'''

Strings can be created by enclosing the characters inside a singal quote or double quote or triple quotes
but in python we generally use tripple quotes to represent the multi-line strigs ,multi-line comments 
and doc-strings.

'''

message_01 = '''This is an another way to create the string using triple quotes '''
message_02 = ' This is also another way to create the strings using single quotes !!!'
message_03 = "Well I guess you are well familer with double quotes"

# --------------------------------------------------------
#       HOW TO ACCESS THE CHARCTERS IN THE STRING
# --------------------------------------------------------

string_name = "Raju Shyam Baburao"
print(string_name)

# Acessing string via indexing 
print(string_name[0])
print("String_name[::-1] : ",string_name[::-1])
print("string_name[2:] : ",string_name[2:])



"""
Note that the strings are immutable, means the characters inside the string cannot 
be change once they have been assigned 

We can simply assign different strings to the same name 

"""

"""Uncomment and try to run this code"""
# message = "Hello, #Root user"
# message[7] = "G"
# Python interpreter will throw the following error 
# TypeError : 'str' object does not support items assignment
# which means you can't assign a value to string, if its already asigned

# But you can re-assign the whole string
string_python_version = "Python 3.10"
print("I hate ",string_python_version)
string_python_version = "Python 2.0"
print("I love ",string_python_version)

# You can also delete the whole string using 'del' keyword
del string_python_version 
print("At the end of day it doesn't matter, string_python_version is deleted using 'del' keyword ")

'''
#############################################################
                OEPRATIONS ON STRING 
#############################################################
    
    1. Concatination    : + operator
    2. lowerCase
    3. uppercase
    4. .join
    5. find
    6. replace
'''
message_01 = "One"
message_02 = "Plus"
Brand_name = message_01 + " " + message_02 
print(Brand_name)


# BOLD relation between string and for loop , use it BABY ;)
string_sample = "This is just not a string it's MY LIFE, How MY LIFE is amazing and IM really GREATFULL for MY LIFE "
int_count = int(0)

for sample in string_sample :
    if(sample == "M"):
        int_count+=1
print(int_count)


int_count = int(0)

# BOLD relation between LIST and for loop , use it BABY ;)

sample_password_list = ["helohelo","rockyou","phoenix600","Khownshu","ShumaGoraot","Kakarot","helohelo","GOD-KNOWS","RESOS^(PROP","helohelo"]
print(sample_password_list)
for sample_list in sample_password_list :
    if sample_list == "helohelo" :
        int_count+=1

print(int_count)
print(f"{int_count} this many times people have used this common passwords out of 10 times")

# We can also check , if a substring exits within a string or not using the keyword 'in'

print(" 'MY LIFE' is  Presient in the string : ","MY LIFE" in string_sample)

print(" 'GF' in present in the string : ","GF" in string_sample)

"""
    BUILT IN FUNCTIONS FOR STRING 
    len() to return the lenght of the string 
    enumerate() : @enumeratre() function returns the enumerate object, it contains the index 
    and values of all items in the string as pairs 
"""

my_priorities = ["GETTING HIGHLY SKILLED TECHNINCAL ","Improve my communication","ETC subject","Girlfriend"]
print(list((enumerate(my_priorities))))
print(f"The lenght of the string is {len(my_priorities)}")
