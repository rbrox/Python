#   Write a program that reads a list of temperatures from a file 
#   called temps.txt, converts those temperatures to Fahrenheit, 
#   and writes the results to a file called ftemps.txt.

def main():
    temp = open('temps.txt', 'r')
    
    temp_list = []
    for unit in temp:
        
        unit = unit.strip()
        temp_list.append(float(unit))
        
    print(temp_list)
    ftemp = open('ftemps.txt', 'w')
    
    for i in temp_list:
        j = i * (9/5) + 32
        ftemp.write(f'{j}\n')
    
main()