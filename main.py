import random

def game(comp, you): # Declaring a game function
    if comp == you:
        return None # This function will return none means it is a tie game
    
    # Checking for all posibilities when computer chooses 's':
    elif comp == 's': # Assigning value to comp variable
        if you == 'p':
            return True # This function will return true if you win
        elif you == 'sc':
            return False # This function will return false if you lose
    
    # Checking for all posibilities when computer choose 'p':
    elif comp == 'p':
        if you == 'sc':
            return True
        elif you == 's':
            return False
    
    # Checking for all posibilities when computer choose 'sc':
    elif comp == 'sc':
        if you == 's':
            return True
        elif you == 'p':
            return False
        

# Asking computer's choice by using random module
randNo = random.randint(1,3)
print("Computer's Turn: Stone(s), Paper(p) or Scissor(sc)??") 

# Declaring computer's choice by using shortcut
if randNo == 1: 
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sc'

# Asking user's input
you = input("Your Turn: Stone(1), Paper(2) or Scissor(3)??") 

# Calling the game function
a = game(comp, you) 

# Printing the choice of Computer
print(f"Computer's choice: {comp}")

# Printing the choice of User
print(f"Your choice: {you}") 

# Declaring the final result and verifying all the posibilities
if a == None:  
    print("This game is Tie!")

elif a:
    print("You Win!")

else:
    print("You Lose!")