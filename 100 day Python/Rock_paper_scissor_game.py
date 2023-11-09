import random
import sys

play = int(input("rock or paper or scissor? 0, 1, or 2 respectively. \n"))
if play == 0:
    print("You chose: rock")
elif play == 1:
    print("You chose: paper")
elif play == 2:
    print("You chose: scissor")
else:
    print("You typed an invalid number. Please type 0, 1 or 2")
    sys.exit()

comp = random.randint(0, 2)
if comp == 0:
    print("Computer chose: ROCK")
elif comp == 1:
    print("Computer chose: PAPER")
else:
    print("Computer chose: SCISSOR")

if play == comp:
    print("It's a tie")
    
elif play == 0:
    if comp == 1:
        print("You lose!")
    else:
        print("You win!")

elif play == 1:
    if comp == 0:
        print("You win!")
    else:
        print("You lose!")
        
else:
    if comp == 0:
        print("You lose!")
    else:
        print("You win!")

