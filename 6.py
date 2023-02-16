
#   Generate a random number between 1 and 10. Ask the user to guess the number 
#   and print a message based on whether they get it right or not.

import random

def main():
    x = random.randint(1, 10)
    
    while True:
        try:
            y = int(input('Enter guess: '))
        
        except ValueError:
            print('Not a number')
        
        else:
            print(y == x)
            if y == x:
                break
            
main()