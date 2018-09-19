"""import random
x = random.randint(-5, 5)
print(x)"""

'''import random
for x in range(500):
    print (random.randint(0,100))
    print(x)'''
    
"""import random
x = random.randint(1,100)
print(x)
if ((x%2) == 1):
    print("This number is odd.")
if ((x%2) == 0):
    print("This number is even.")"""
    
import random
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

"""Write the same block of code in a function and call that function 10 times"""

def EvenOdd():
    


 

