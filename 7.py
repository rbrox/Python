#   Write a program that asks the user for two numbers and
#   prints Close if the numbers are within .001 of each other 
#   and not close otherwise.

def main():
    x = float(input('Enter 1st num: '))
    y = float(input('Enter 2nd num: '))
    
    if x < y:
        t = x
        x = y
        y = t
        
    if x - y < 0.001 and x - y > 0:
        print('Close')

    else:
        print('Not close')
        
main()