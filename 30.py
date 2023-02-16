#   Write a class called Converter. 
#   The user will pass a length and a unit when declaring an object from 
#   the class—for example, c = Converter (9,'inches'). 
#   The possible units are inches, feet, yards, miles, kilometers, 
#   meters, centimeters, and millimeters. For each of these units 
#   there should be a method that returns the length converted into those units. 
#   For example, using the Converter object created above, 
#   the user could call c.feet() and should get 0.75 as the result.

scale = {
    'feet' : 1,
    'inch' : 12,
    'yard' : 0.333,
    'mile' : 0.00018939375,
    'mm'   : 304.7996952,
    'cm'   : 30.47996952,
    'metre': 0.3047996952,
    'km'   : 0.0003047996952,

}

class Converter:
    feet = 0
    
    
    
    def __init__(self, mes, type):
        self.type = type
        #self.index = scale(type)
        self.feet = mes / scale(type)
        

def main():
    feet = Converter(12, 'inch')
    print(feet.feet)
    
main()