#   Write a function called first_diff that is given 
#   two strings and returns the first location in which the strings differ. 
#   If the strings are identical, it should return -1.

def main():
    str1 = input('Enter: ')
    str2 = input('Enter: ')
    
    print(first_diff(str1, str2))
    

def first_diff(str1, str2):
    
    for i in range(len(str1)):
        try:
            if not (str1[i] == str2[i]):
                return i 
        except IndexError:
            return i     
    return -1

main()