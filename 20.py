#   Write a function called is_sortedthat is given a list 
#   and returns True if the list is sorted and False otherwise.

def main():
    
    lis = []
    for _ in range(5):
        x = input('Enter: ')
        lis.append(x)
    
    sor_lis = lis
    print(lis, sor_lis)
    if sor_lis == lis:
            
        print('lis was sorted')
    else:
        print('lis was not sorted')
            
main()