#   Use a forloop to print a triangle like the one below. 
#   Allow the user to specify how high the triangle should be.


def main():
    x = int(input('Enter triangle height: '))
    triangle(x)
    
def triangle(x):
    y = 2 * x - 1
    for i in range(x):
        for j in range(y):
            if (i + j) % 2 == 1 and j ???:
                print('*',end= '')
            else :
                print('_', end= '')                
        print('')            


main()