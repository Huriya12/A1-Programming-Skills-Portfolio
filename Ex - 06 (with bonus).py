# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:45:55 2024

@author: 97156
"""
"""
Exercise 6: Control Structures
"""
password=12345 #Variable for correct password
attempts=5 #Variable for maximum attempts

#While Loop that keeps on going until the correct password is entered
while True:
    user_input=int(input("Please enter the password: ")) #User input
    attempts-=1 #Decrements the attempts by 1
    
    
    if user_input==password: #If correct password is entered
        print("You have successfully entered the correct password.") #Prints message to the console
        break #Exits the loop
    
    elif attempts>0:  #If there are still remaining attempts left greater than 0
        print("Incorrect Password. Please try again.") #Prints message to the console
        print(f"You have {{{attempts}}} left.") #Prints the remaining attempts to the console
        
    else: #If all attempts are used
        print("Access Not Granted.") #Prints message to the console
        print("The authorities have been alerted to possible unauthorized data access.") #Prints message to the console
        break #Exits the loop