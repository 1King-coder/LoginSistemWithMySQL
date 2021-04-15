import smtplib
from string import Template
from random import randint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .EmailAccount import Email_account


class SendEmail:
    def __init__(self, code, username, user_email):
        self.code = code
        self.username = username
        self.user_email = user_email

    @staticmethod
    def set_template(code):
        with open('./SendCode/template.html', 'r') as html:
            template = Template(html.read())
            body = template.substitute(Code=code)
            return body

    def set_email(self):
        body = self.set_template(self.code)
        message = MIMEMultipart()
        message['from'] = "Vitor's Login System"
        message['subject'] = self.username
        message.attach(MIMEText(body, 'html'))
        return message

    def send_email(self):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.ehlo()
            server.starttls()
            server.login(Email_account['email'], Email_account['password'])
            server.send_message(self.set_email(), to_addrs=self.user_email)
