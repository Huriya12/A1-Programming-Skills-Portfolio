# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:20:59 2024

@author: 97156
"""
"""
Exercise 10: Functions
"""
#First function
def even_odd(number):
    
    #Checks if the number provided is divisible by 2 and if the remainder is 0
    if (number % 2) == 0: #If true
        return f"The number {{{number}}} is an even number." #Return this message
    
    else: #If false
        return f"The number {{{number}}} is an odd number." #Return this message

#Main function
def main():
    
    number_entered=int(input("Please enter a number: ")) #User Input
    final_result=even_odd(number_entered) #Calls for the previous function and fetches the results
    print(final_result) #Prints final result to the console

if __name__ == "__main__":
    main()
    