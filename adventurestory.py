import time
name = input("To begin our journey, what is your name? ")

def greeting():
    print("Salutations " + name + ".")
    print("Your story begins on a perfectly average Sunday and you, " + name + ", are a perfectly average person...")
    time.sleep(2)
    print("However at precisely 7:36PM, something changes. Thoughts of Frosted Flakes consume your mind, everything has narrowed down to the prospect of one (1) bowl of cereal.")
    print("You decide to power walk down to your kitchen.")
    print("You find the cereal, the bowl, the spoon but the time comes to seek the milk...")
    time.sleep(2)
    print("It's not there? How could this be? You're out of milk.")
    actDepression()

def actDepression():
    decision1 = int(input("Well, " + name + ", do you act upon your craving or reppress it like all other emotions in your life? Type '1' for act or '2' for reppress: "))
    if (decision1 == 1): 
        print("Because of your craving, you decide to go the store.")
        atStore()
    else:
        print("Reconsider your life choices. You will have to go to the store like a functioning human.")
        actDepression()
    
    
def atStore():
    print("As you amble your way to the dairy section...something is wrong. Row after row of empty milk shelves approach you. You must make a decision. ")
    decision2 = int(input("Do you ask an associate if there is any milk in the back room or do you have a tantrum? Type '1' for ask or '2' for tantrum: "))
    if (decision2 == 1):
        print("You ask an associate and he tells you to follow him to the storage room.")
        soyOr2percent()
    else:
        print("Are you done? Pick yourself off the floor and use those defunct social skills.")
        atStore()
        
def soyOr2percent():
    print("The associate leads you to an unmarked door at the back of the store. He unlocks the door, revealing a massive warehouse filled with...milk? At last, the end is near and the milk is here. But the associate is now attempting to get your attention. He asks you a question: 'So you want soy or 2%?' ")
    decision3 = int(input("Type '1' for soy or '2' for 2%:"))
    if (decision3 == 1):
        print("Compras la botella de leche y luego vuelves a tu casa. Pones la botella de leche arriba del mostrador, y buscas por el cereal. Encuentras la caja de Frosted Flakes. Sacudes la caja... y una escama solitaria se cae de la caja. La vida no tiene sentido.")
    elif (decision3 == 2):
        print("You buy the bottle of milk and return home. You set your hard-won milk on the kitchen counter, now searching for the cereal. You find the box of Frosted Flakes. You shake out the box...and one solitary flake falls out. Life is meaningless. ")
    else:
        print("Try again. Intentalo de nuevo.")
        soyOr2percent()


    
    
        
greeting()



