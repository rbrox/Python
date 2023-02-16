# Write a program that asks the user to enter a word
# and prints out whether that word contains any vowels.

vowel = ['a', 'e', 'i', 'o', 'u']

def main():
    word = input('Enter: ')
    
    
    for c in word:
        if c in vowel:
            print('Contains vowles')
            return
    
    print('No vowles')            
    
main()    