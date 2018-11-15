import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host= "smtp.gmail.com"
port= 587
username="m.tahircis95@gmail.com"
password="safamaha444"
from_email="babloo9814@gmail.com"
to_list = ["tahirs95@hotmail.com"]
email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
# try:
#     email_conn.login(username,password)
#     email_conn.sendmail(from_email, to_list, "hello buddy")
# except:
#     print("hello")
# email_conn.quit()
the_msg = MIMEMultipart("alternative")
the_msg['Subject']='Hello'
the_msg['From']=from_email
# the_msg['To']=to_list[0]
plain_txt = "Testing the message"
html_txt = """
<html>
<head> </head>
<body>
<p> hey 
<a href='https://www.google.com/'> Google </a>
</p>
</body>
</html>
"""
part1= MIMEText(plain_txt, 'plain')
part2= MIMEText(html_txt,'html')
the_msg.attach(part1)
the_msg.attach(part2)
email_conn.sendmail(from_email, to_list, the_msg.as_string())
email_conn.quit()
