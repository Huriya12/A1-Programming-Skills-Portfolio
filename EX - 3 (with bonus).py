# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:40:45 2024

@author: 97156
"""
"""
Exercise 3: Dictionary
"""
name=str(input("Enter your full name:")) #User input for name
hometown=str(input("Enter your hometown:")) #User input for hometown


#While loop that keeps on going until a valid integer value is entered
while True:
    age=input("Enter your age (Please enter a numerical value):") #User input for age
    
    #Checks if the input is valid integer value
    if age.isdigit(): #If true
        age=int(age) #Converts the string "age" into integer
        break #Exits loop
        
    else: #If false
        print("Invalid Input. Please enter a numerical value.") #Prints message to the console
        continue #Continues the loop until the condition is met
        

#Stores user input's information in a dictionary
user_input={'Name': name,
           'Hometown': hometown,
           'Age': age}


#Print values on seperate lines within a single print statement by typing newline character or (\n)
print("Name:", user_input['Name'],"\nHometown:", user_input['Hometown'],"\nAge:", user_input['Age']) 