name = input("Hello! WHat is your name?: ")
print ("Nice to meet you " + (name) + ("! My name is Python III."))
print ('Today, I am going to ask you to enter the lengths of the legs of a triangle for a, b, and c.')
print ('With these values, I am going to determine whether the shape you created is a right, obtuse, or an acute triangle.')
print ('I may even determine whether you created a triangle that does not exist!')
a = float(input('First, enter a value for the length of a: '))
b = float(input('Now, enter a value for the length of b: '))
c = float(input('Lastly, enter a value for the length of c: '))

if int(c > a + b):
    print('Oh no! These lengths do not create a triangle!')
if int(c == ((a**2)+(b**2))**(1/2)):
    print('These values make a right triangle!')
if int(c > ((a**2)+(b**2))**(1/2)):
    print('These values make an obtuse triangle!')
if int(c < ((a**2)+(b**2))**(1/2)):
    print('These values make an acute triangle!')
    
