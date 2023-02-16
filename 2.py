
#   Write a program that asks the user to enter three numbers
#   (use three separate input statements). 
#   Create variables called total and average that hold the 
#   sum and average of the three numbers and print out the values 
#   of total and average.


def main():
    
    iterations = 3
    total = 0

    
    for _ in range(iterations):
        try:
            x = int (input("Enter num: "))
        except ValueError:
            pass
        else:
            total += x
    
    print(f'Sum = {total}, Average = {total / iterations : .0f}')


main()    