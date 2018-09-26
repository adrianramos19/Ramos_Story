""" 
This all about functions and how they work
"""
def greeting():           #this function does not return anything
    print("Hello world")

def askname():
    name = input("What is your name? ")
    return name
    
def askage():
    age = int(input("What is your age? ")) #write a function that asks for their age AND returns how old they are
    return age 
    
def canvote(age):
    if (age >= 18):
        print("You can vote!")
        canvote = True
    else:
        print("Sorry you can't vote!")
        canvote = False
    return canvote

#call the function
greeting()
x = askname()
print("Hello " + x)  #save the output of askaname() to variable

y = askage()   #y = age
z = canvote(y)  #z = if they can vote or not
print(z)

