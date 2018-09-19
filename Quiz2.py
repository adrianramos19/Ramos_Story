"""Write the same block of code in a function and call that function 10 times"""
import random

def EvenOdd():
    even = 0 
    odd = 0
    for l in range(10):
        x = random.randint(1,100)
        if ((x%2) == 1):
            print("The number " + str(x) + " is odd.")
            odd = int(odd+1)
        if ((x%2) == 0):
            print("The number " + str(x) + " is even.")
            even = int(even+1)
    print("The number of odds that occurred is " + str(odd) + ("!"))
    print("The number of odds that occurred is " + str(even) + ("!"))
    
def greeting():
    name = input("Hello there! My name is Python III! What is your name?: ")
    print("Hello " + name + ("!"))
    
def age():
    age = int(input("How old are you dude?: "))
    return age