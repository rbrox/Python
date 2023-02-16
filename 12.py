#   Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list
# (e) Print how many even numbers are in the list.

import random

def main():
    lis = []
    avg = 0
    even_count = 0
    # genarate list
    for _ in range(20):
        ele = random.randint(1, 100)
        lis.append(ele)
        
        # b.
        avg += ele
        
        # e.
        if ele % 2 == 0:
            even_count += 1
        
    # a. print list
    print(lis)        
        
    print(f'Avg = {avg / 20}')
        
    print(f'Even count = {even_count}')
    
    
        
    print(sorted(lis))
        
        
main()        