#   Write a program that asks the user to enter two strings of the same length. 
#   The program should then check to see if the strings are of the same length. 
#   If they are not, the program should print an appropriate message and exit. 
#   If they are of the same length, the program should alternate the characters of the two strings. 
#   For example, if the user enters abcdeandABCDE the program should print out AaBbCcDdEe.


def main():
    x = (input('Enter 1st string: '))
    y = (input('Enter 2nd string: '))
    
    if len(x) == len(y) :
        z = ''
        a = 0
        b = 0
        
        for i in range(len(x) * 2):
            
            if i % 2 == 0:
                z += y[a]
                a += 1
            
            else:
                z += x[b]
                b += 1              
        
        print(z)
        
    else:
        print('Strings are not of same length')        
main()        