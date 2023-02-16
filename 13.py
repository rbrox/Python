#   Write a program that asks the user for an integer and creates a list 
#   that consists of the factors of that integer.

def main():
    lis = []
    x = int(input('Enter int: '))
    
    for i in range(1, x+1):
        
        if x % i == 0:
            lis.append(i)

    print(lis)
    print(len(lis))
    
main()