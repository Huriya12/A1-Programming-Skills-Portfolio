# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:41:41 2024

@author: 97156
"""
"""
Exercise 4: Control Structures
"""
first_question=str(input("What is the capital of France? ")) #User input
answer="Paris" #Correct answer


#Checks if the user input is correct
#If true
if first_question.lower()==answer.lower(): #Converts both values to lowercase to prevent case sensitivity
    print("Oui! Your answer is indeed correct.") #Print message to the console
    
#If false
else:
    print("Non... The answer is", answer,".") #Print message to the console
    
    
#Extended Quiz:
#Dictionary which stores all capitals of 10 European countries
capitals={"Norway":"Oslo",
         "Ireland":"Dublin",
         "Romania":"Bucharest",
         "Denmark":"Copenhagen",
         "Bulgaria":"Sofia",
         "Finland":"Helsinki",
         "Portugal":"Lisbon",
         "Belgium":"Brussels",
         "Greece":"Athens",
         "United Kingdom":"London"}

#For loop through dictionary:
for country in capitals:
    questions=str(input(f"What is the capital of {{{country}}} ? ")) #User input
    
    #If true
    if questions.lower()==capitals[country].lower(): #Converts both values to lowercase to prevent case sensitivity
        print("Oui! Your answer is correct yet again.") #Print message to the console
        
    #If false
    else:
        print(f"Non... The answer is {{{capitals[country]}}}.") #Print message to the console