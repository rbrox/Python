#   Write a program that asks the user for their name and how many times to print it.
#   The program should print out the user’s name the specified number of times.


def main():
    name = input('Enter your name: ')
    x = int(input('Enter number of times you would like to print your name: '))
    
    for _ in range (x):
        print(name)
        
main()        