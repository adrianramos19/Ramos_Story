"""
Write a program that will take a number (Integers only) and return a statement tha will let the user know if it is even or odd
"""

number = int(input ('Pick a number, any number: '))
if (number%2) == (0) : 
    print ('The number ' + str(number) + ( ' is even.'))
    
if (number%2) == (1) :
    print ('The number ' + str(number) + (' is odd.'))
    


 
