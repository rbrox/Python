#   Write a function called merge that takes two already sorted lists 
#   of possibly different lengths, and merges them into a single sorted list.
# (a) Do this using the sort method. 
# (b) Do this without using the sort method.

def main():
    list1 = [1,2,4,6,8,9]
    list2 = [5,7,10,11]
    print(merge(list1, list2))


def merge(list_1, list_2):
    list_c = []
    x = 0
    y = 0
    for i in range(len(list_1) + len(list_2)):
        
        if list_1[x] > list_2[y]:
            list_c.append(list_2[y])
            y += 1
            
            if y == len(list_2):
                
                while x < len(list_1):
                    list_c.append(list_1[x])
                    x += 1
                return list_c
        
        else:
            list_c.append(list_1[x])
            x += 1
            
            if x == len(list_1):
                while y < len(list_2):
                    list_c.append(list_2[y])
                    y += 1
                return list_c
    
    
main()