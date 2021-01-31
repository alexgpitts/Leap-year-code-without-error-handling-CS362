
'''
Author: Alex Pitts
Date: 1/15/21
Class: CS 362

Description: This program simply calculates if a user inputted year is a leap year.

Edited: 1/30/21


'''


print("This software is designed to calculate if a year is a leap year")



year = int(input("\nPlease enter a year: ")) #get year input from user
    
if(year%4 == 0): #evenly divisible by 4?
    if(year%100 == 0):#evenly divisible by 100?
        if(year%400 == 0):#evenly divisible by 400?
            print(year, "is a leap year\n")
        else:
            print(year, "is not a leap year\n")
    else: 
        print(year, "is a leap year\n")
else:
    print(year, "is not a leap year\n")

input("Press Enter to close...")