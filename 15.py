#   Write a program that removes any repeated items from a list 
#   so that each item appears at most once. 
#   For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

def main():
    
    lis = []
    for _ in range(5):
        x = input('Enter: ')
        lis.append(x)
        
    print(lis)
    print(set(lis))
    
main()