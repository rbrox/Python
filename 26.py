#   Write a program that reads a file consisting of email addresses, 
#   each on its own line. Your program should print out a string 
#   consisting of those email addresses separated by semicolons.
    
def main():
    emails = open('emails.txt', 'r')
    
    for mail in emails:
        mail = mail.replace('\n', '\t')
        print(mail, end=';')
        
main()