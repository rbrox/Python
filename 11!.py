#   In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or 3(x+5). 
#   Computers prefer those expressions to include the multiplication symbol, like 3*x+4*y or 3*(x+5). 
#   Write a program that asks the user for an algebraic expression and then inserts multiplication symbols where appropriate.

oper = ['+', '-', '*', '/']

def main():
    exp = input("Enter: ")
    print(lis(exp), sep='*')
    
def lis(exp):
    
    terms = []
    operators = []
    
    for i in exp:
       if i.isanum??????    

main()