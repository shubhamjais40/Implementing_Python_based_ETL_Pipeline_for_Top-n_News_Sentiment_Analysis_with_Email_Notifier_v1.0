#mail function
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pretty_html_table import build_table
import smtplib
import ssl
from common import *


def do_email(to_mail):
    news_table=to_mail
    news_set=news_table.drop(columns=["pos","neu","neg","ids"])
    
    #mail parameters variables
    message = MIMEMultipart()
    message['Subject'] ="Top 5 news Headline of recent hr"
    message['From'] = sender
    message['To'] =receiver
    
    #mail content variables
    #using pretty_html_table lib to format html table
    body_content = build_table(news_set, 'blue_dark',font_size='small')
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()
    
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,msg_body)
        
    return 0
