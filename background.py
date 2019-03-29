from background_task import background
from django.shortcuts import render,HttpResponse
import smtplib
import time
import schedule


@background(queue='ai_reviewer')
def email_sender():
    print(str(time.strftime('%H:%M')))
    if str(time.strftime('%H:%M')) == '11:39':
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        s.ehlo()
        s.starttls() 
        
        # Authentication 
        s.login("m.tahircis95@gmail.com", "safamaha444") 
        
        # message to be sent 
        message = "Message_you_need_to_send"
        
        # sending the mail 
        s.sendmail("sender_email_id", "tahirs95@hotmail.com", message) 
        
        # terminating the session 
        s.quit()
        print("Email done at", str(time.strftime('%H:%M'))) 
    else:
        print('Waiting')
        


def background_view(request):
    email_sender(repeat=120)
    return HttpResponse("Email sent")


def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
time.sleep(1)

while True:
    schedule.run_pending()
    time.sleep(1)


  
