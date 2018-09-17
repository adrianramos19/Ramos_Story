name = input('Hello! What is your name? ')

print("Pleasure meeting you " + name + ". I hope you're enjoying your day! My name is Python III.")
print('Today, I will be helping you solve a right triangle using the Pythagorean Theorem.')

print("First, I'm going to ask you to enter the lengths of the legs 'a' and 'b' of a right triangle.")

a = float(input ('Enter any number for the length of a: '))
b = float(input ('Enter any number for the legnth of b: '))
print ("The hypotenuse of a right triangle when 'a' equals " + str(a) + (" and 'b' equals ") + str(b) + (" is ") + str((a**2 + b**2)**(1/2)) + (" units."))
