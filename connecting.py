# Note- some email such as gmail we need to set the settings to less secure only then we can use this script to send mails 
import smtplib
file1 = open(r"C:\Users\WIN 10\Desktop\email.txt","r")    #location of text file 
a = file1.readlines()
b = []
for email in a:
    b.append(email.strip("\n"))
print(b)
sender = "email"             #your email    
passcode = "password here"   #your password
for i in range(0,len(b)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, passcode)
    message = "message"
    s.sendmail("sender_email_id", b[i], message)
    s.quit()
