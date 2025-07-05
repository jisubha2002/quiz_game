import smtplib as sm
ob = sm.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('jisubha2005@gmail.com','jisubha@123')
subject = "test python"
body ="hello python"
massage = "subject :{}\n\n{}".format(subject,body)
listadd =['subhankarmaji739@gmail.com']
ob.sendmail('jisubha2005@gmail.com',listadd,massage)
print("mail send")
ob.quit()