#   Write a class called Time whose only field is a time in seconds. 
#   It should have a method called convert_to_minutes 
#   that returns a string of minutes and seconds formatted 
#   as in the following example: if seconds is 230, 
#   the method should return '5:50'. 
#   It should also have a method called 
#   convert_to_hoursthat returns a string of hours, minutes, and seconds 
#   formatted analogously to the previous method.

class Time:
    time = 0
    
    def __init__ (self, time):
        self.time = time

    def convert_to_min(self):
        min = self.time // 60
        sec = self.time % 60
        
        return f'{min}:{sec}'
    
    def convert_to_hour(self):
        hour = self.time // 3600
        min = self.time // 60
        sec = self.time % 60 
        
        return f'{hour}:{min}:{sec}'
        

def main():
    timer = Time(3612)
    print(timer.convert_to_min())
    print(timer.convert_to_hour())

main()