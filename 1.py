
#   Write a program that asks the user for a weight in kilograms
#   and converts it to pounds. There are 2.2 pounds in a kilogram.


def main():
    try:
        kilos = int(input("Enter weight in kilos: "))
    except ValueError:
        print('Enter numeric')
    else:
        print(f'Weight in pounds {pounds(kilos): .01f}')


def pounds(kilos):
    return kilos * 2.2

main()
