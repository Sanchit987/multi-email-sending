import smtplib
file1 = open(r"C:\Users\WIN 10\Desktop\email.txt","r")
a = file1.readlines()
b = []
for email in a:
    b.append(email.strip("\n"))
print(b)
sender = "email"
passcode = "password here"
for i in range(0,len(b)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, passcode)
    message = "message"
    s.sendmail("sender_email_id", b[i], message)
    s.quit()