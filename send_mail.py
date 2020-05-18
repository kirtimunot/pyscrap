import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add='jain.kirti13@gmail.com'
    to_add='kirtimunot@rediffmail.com'
    sub="Finance report"

    msg=MIMEMultipart()
    msg['from']=from_add
    msg['To']=to_add
    msg['subject']=sub

    body="<b>hey!!!! Todays finance report</b>"
    msg.attach(MIMEText(body,'html'))
    myfile=open(filename,'rb')
    part=MIMEBase('application','octet-stream')
    part.set_payload((myfile).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment;filename='+filename)
    msg.attach(part)

    message=msg.as_string()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_add,'ftehukruiytkhrlb')
    #msg="hey mail using python script"
    server.sendmail(from_add,to_add,message)

    server.quit()