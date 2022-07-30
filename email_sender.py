import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Shivangi Sood'
email['to'] = 'soodshivangi@yahoo.com'
email['subject'] = 'You won $10,000! Congratulations!'

email.set_content('Gotcha! This was a spam email ;)')

with smtplib.SMTP(host='smtp.mail.yahoo.com', port=465) as smtp: #port can vary depending on your email service provider
	smtp.ehlo()
	smtp.starttls()
	smtp.login('soodshivangi@yahoo.com', '********') #enter your email id and password here
	smtp.send_message(email)
	print('DONE!')