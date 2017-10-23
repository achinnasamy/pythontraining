
import os

# A simple print statement.
# You can use a single quote or double quote
print ('Hello Chola')
print ("Hello Chola")

# Single comment

#''' Three quotes for multi line comment
''' 
Multiline 

        comment
'''

# String can be assigned with single or double quotes
string_variable = 'Aravindh'
another_string_varibale = "Chinnasamy"

# String concatenation
my_name = string_variable + another_string_varibale

print(my_name)
''' 
Data types in python:

    Numbers
    Strings
    Lists
    Tuples
    Dictionary
'''

number_variable = 2016

''' Arithmetic Operations '''
addition = 2 + 2
subtraction = 5 - 3
multiplication = 5 * 6
division = 4 / 2
remainder = 5 % 3
square = 2 ** 3
quotient = 5  % 3

# Formatting a print statement
print("Addition = %s" % "hi")
print("Addition = %s" % addition)

# Priting new lines 5 times
print("\n" * 5)


# Creating list

investment_banking_contrats_list = ['contrats_1',
                                    'echienear', 'ib_202']
retail_banking_france = ['bddf', 'gbis', 'embargo']

concatenated_list = investment_banking_contrats_list + retail_banking_france

investment_banking_contrats_list[0] = 'contrats_22'
print(investment_banking_contrats_list)
print(investment_banking_contrats_list[0])
print(investment_banking_contrats_list[1:2])
print(concatenated_list)

my_personal_events = ['make my food', 'fill petrol', "atm withdraw", 'visit client']

# Lists containing many lists
combine_lists = [my_personal_events, investment_banking_contrats_list]

print(combine_lists)
print(combine_lists[1][1])

investment_banking_contrats_list.append("all_contract")
investment_banking_contrats_list.insert(1, "timeline_contract")


print(len(investment_banking_contrats_list))
print(max(investment_banking_contrats_list))
print(min(investment_banking_contrats_list))


# Tuple

pi_tuple = (3,1,4,1,5,9)
pi_string_tuple = ("three", "one", "four", "one", "five", "nine")

# Tuple to list
pi_list = list(pi_tuple)

# List to tuple
pi_tuple_new = tuple(pi_list)

print("%s %s %s" % (len(pi_tuple), max(pi_tuple), min(pi_tuple)))



# Dictionary


country_code_dic = {"IN" : "India",
                    "SL": "Srilanka",
                    "CA": "Cameroon",
                    "_": "Default"}



print(country_code_dic["IN"])

print(country_code_dic["IN"])


country_code_dic["IN"] = "Hindhusthan"


print(country_code_dic["IN"])
del country_code_dic["IN"]
#print(country_code_dic["IN"])


print(country_code_dic.get("IN"))
print(country_code_dic.keys())
print(country_code_dic.values())


# Set

set_of_integers = set([1,2,4,4,2,5,6,2,1])
print ("Printing a set %s" % set_of_integers)


set_of_frozen_list = frozenset([1,2,4,3,2,3,2,1,7,9,7,8])
print ("Printing a frozen set %s" % set_of_frozen_list)

# Conditionals

# if else elif == != > >= < <=


age = 30

if (age > 19):
    print("You are a teenager")
else:
 print("You are not a teenager")



# Logical Operators : and or not
