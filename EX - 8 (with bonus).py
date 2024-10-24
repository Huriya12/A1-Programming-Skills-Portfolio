# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:51:57 2024

@author: 97156
"""
"""
Exercise 8: List
"""
#Predefined list of names
names=["Jake","Zac","Ian","Ron","Sam","Dave"]

#User Input
search=str(input("Please enter a name: "))

#Checks if the input matched any of the names in the list
if search in names: #If true
    print("The name,", search, "is on the list.") #Print message to the console
    
else: #If false
    print("The name,", search, "is not on the list.") #Print message to the console

