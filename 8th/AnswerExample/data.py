import csv
from email.message import EmailMessage
from email.generator import Generator

#メール本文用テキスト
def read_txt(path):
    with open(path,'r',encoding='utf-8') as f:
        return f.read()

def create_mail(subject, to_addr, cc_addr, from_addr, body_txt):
    mail_data = EmailMessage()
    mail_data["subject"] = subject
    mail_data["To"] = to_addr
    mail_data["CC"] = cc_addr
    mail_data["From"] = from_addr
    mail_data.set_content(body_txt)
    return mail_data



