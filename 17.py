#   Write a function called sum_digitsthat 
#   is given an integer num and returns the sum of the digits of num.

def main():
    x = (input('Enter: '))
    sum = 0
    
    for i in x:
        sum += int(i)
        
    print('Sum of digits:' ,sum)
    

main()