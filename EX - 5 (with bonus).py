# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:27:41 2024

@author: 97156
"""
"""
Exercise 5: Dictionary
"""
#Dictionary that stores month number (1-12) and its number of days
calendar={1:31,
          2:28,
          3:31,
          4:30,
          5:31,
          6:30,
          7:31,
          8:31,
          9:30,
          10:31,
          11:30,
          12:31}

#User input for month number
month=int(input("Please enter the month number: "))

#Checks if the input matches the values in the calendar
if month in calendar: #If valid

    
    #If month number is 2, check for leap year
    if month==2:
        leap_year=int(input("Please enter the year: ")) #User input for the year
        
    if (leap_year%400==0) or (leap_year%100!=0) and (leap_year%4==0):  #If true
        print("This year's February in indeed a leap year.") #Print message to the console
        print(f"This month have {{{calendar[month]+1}}} days") #Adjust number of days to 29
        
    else: #If false
        print("This year's February is not a leap year.") #Print message to the console
        
        
    print(f"This month have {{{calendar[month]}}} days") #Print number of days to the console

else: #If invalid
    print("Invalid Input. Please try again.") #Print message to the console



