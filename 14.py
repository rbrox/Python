#   Write a program that generates 100 random integers that are either 0 or 1. 
#   Then find the longest run of zeros, the largest number of zeros in a row. 
#   For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.


import random

def main():
    lis = []
    zero_count = 0
    count = 0
    for _ in range(100):
        ele = random.randint(0,1)
        lis.append(ele)
        
        if ele == 0:
            count += 1
        
        else:
            if count > zero_count:
                zero_count = count
            
            count = 0
            
    if count > zero_count:
                zero_count = count   
    print(lis)
    print(zero_count)
    
main()