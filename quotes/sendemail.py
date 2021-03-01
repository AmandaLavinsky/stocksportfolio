import smtplib
my_email="stockportfolio364@gmail.com"
password = "lavinsky1730"
	

def send_email():

	connection = smtplib.SMTP("smtp.gmail.com")
	connection.starttls()
	connection.login(user=my_email,password=password)
	connection.sendmail(from_addr=my_email,to_addrs="stockportfolio364@yahoo.com",msg="Hello")
	connection.close()
