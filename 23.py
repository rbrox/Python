#   Write a function called primes that is given a number n and returns a list of the first n primes. 
#   Let the default value of n be 100.

def primes():
    try :
        x = int(input('Enter: '))
    
    except ValueError:
        x = 100
        pass
    
    for i in range(1, 100):
        count = 0
        for j in range (1, i):
            
            if i % j == 0:
                count += 1
                
        if count <= 2:
            print(i)
        
        
primes()