import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host= "smtp.gmail.com"
port= 587
username="m.tahircis95@gmail.com"
password="safamaha444"
from_email=username
to_list = ["tahirs95@hotmail.com"]

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE"""
    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower() 
        amount = "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
        } 
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None: # if email != None
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail["email"]
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []
    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail["email"]
                user_message = detail["message"]
                email_conn = smtplib.SMTP(host,port)
                email_conn.ehlo()
                email_conn.starttls()
                email_conn.login(username,password)
                the_msg = MIMEMultipart("alternative")
                the_msg['Subject']='Billing Update'
                the_msg['From']=from_email
                the_msg['To']=to_list[0]
                plain_txt = "Testing the message"
                part1= MIMEText(user_message, 'plain')
                the_msg.attach(part1)
                email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                email_conn.quit()
            return True
        return False

obj = MessageUser()
obj.add_user("Justin", 123.32, email='tahirs95@hotmail.com')
obj.add_user("jOhn", 94.23, email='tahirs95@hotmail.com')
obj.add_user("Sean", 93.23, email='tahirs95@hotmail.com')
obj.add_user("Emilee", 193.23, email='tahirs95@hotmail.com')
obj.add_user("Marie", 13.23, email='tahirs95@hotmail.com')
obj.send_email()





default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            """
            Here's a simple solution to capitalize 
            everyone's name prior to sending
            """
            name = name[0].upper() + name[1:].lower() 

            """
            Did you get the bonus??
            """
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total=new_amount
                )
            i += 1
            print(new_msg)



make_messages(default_names, default_amounts)



def append_data(file_path, name, email, amount):
    fieldnames=['id', 'name', 'email','amount','sent','date']
    next_id = get_length(file_path)
    with open("data.csv", "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            "sent": '',
            "amount": amount,
            "date": datetime.datetime.now()
          })

append_data("data.csv","Tahir","tahirs95@hotmail.com", 123.44)

filename = "data.csv"
temp_file = NamedTemporaryFile(mode='w', delete=False)
with open(filename, "rt",newline='') as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames=['id', 'name', 'email','amount','sent']
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    # writer.writeheader()
    print(temp_file.name)
    for row in reader:
        # if int(row['id'])== 4:
        #     row['sent']=True
        #     print(row)
        # writer.writerow(row)
        writer.writerow({
            "id":row["id"],
            "name":row["name"],
            "email":row["email"],
            "amount":1234,
            "sent":''
        })
    shutil.move(temp_file.name, filename)

