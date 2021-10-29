print("Hi Dear! let guess the number from 1 to 100 we have in this *, \n You have only three chance to guess the number. ")
g = 1
while(g<=5):
    print("Enter the number:")
    num = int(input())
    if num<67:
        print("You enter lesser Try Again")
    elif num>67:
        print("You Enter Greater Try Again")
    elif num==67:
        print("Congrats You guessed the number\nThe number is 67!")
        break
    print(g, "Number of gusses attempt")
    g = g + 1
if g>5:
    print("GAME OVER")