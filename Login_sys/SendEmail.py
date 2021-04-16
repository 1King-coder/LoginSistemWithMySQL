import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .Data_base.Data_base import Usuarios
from .SendCode.EmailAccount import Email_account


class SendEmail:
    def __init__(self, code, user_input):
        self.users_db = Usuarios()
        self.code = code
        self.user_input = user_input

    def get_email(self) -> str:
        return self.users_db.get_email(self.user_input)

    def get_username(self) -> str:
        return self.users_db.get_username(self.user_input)

    @staticmethod
    def set_template(code) -> str:
        with open('Login_sys/SendCode/template.html', 'r') as html:
            template = Template(html.read())
            body = template.substitute(Code=code)
            return body

    def set_email(self) -> MIMEMultipart:
        body = self.set_template(self.code)
        message = MIMEMultipart()
        message['from'] = "Vitor's Login System"
        message['subject'] = self.get_username()
        message.attach(MIMEText(body, 'html'))
        return message

    def send_email(self):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.ehlo()
            server.starttls()
            server.login(Email_account['email'], Email_account['password'])
            server.send_message(self.set_email(), to_addrs=self.get_email())
