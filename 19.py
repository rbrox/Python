#   Write a function called number_of_factorsthat takes an integer 
#   and returns how many factors the number has.


def main():
    lis = []
    x = int(input('Enter int: '))
    
    for i in range(1, x+1):
        
        if x % i == 0:
            lis.append(i)

    print(lis)
    print
    
main()