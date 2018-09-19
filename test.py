import Quiz2
Quiz2.greeting()
x = Quiz2.age()    #stores the return value of the function age()

if (x>=18):
    print("You are old enough to vote!")
if (x<18):
    print("In " + str(18 - x) + "years, you will be able to vote!")



