#   Write a program that asks the user to enter a length in feet. 
#   The program should then give the user the option to convert from feet into inches, 
#   yards, miles, millimeters, centimeters, meters, or kilometers. 
#   Say if the user enters a 
#   1, then the program converts to inches, 
#   if they enter a 2, then the program converts to yards, etc. 
#   While this can be done with if statements, it is much shorter with lists and it is also easier to add new conversions if you use lists.

scale = {
    
    'inch' : 12,
    'yard' : 0.333,
    'mile' : 0.00018939375,
    'mm'   : 304.7996952,
    'cm'   : 30.47996952,
    'metre': 0.3047996952,
    'km'   : 0.0003047996952,

}

def main():
    feet = float(input('Enter: '))
    print('Enter conversion key',scale, sep= '\n\n')
    key = input('Key:')
    print(feet*scale[key])
    
main()