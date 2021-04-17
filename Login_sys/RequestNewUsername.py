from .Data_base.Data_base import Usuarios
from .GraphicGui.RequestNewUsernameInterface import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .SendEmail import SendEmail
from .SendCode.Cache import Cache
from .SendCode.GenerateAuthCode import Get_Auth_Code
from .RequestConfirmationCode import Request_Confirmation_Code


class Request_New_Username(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowTitle('Request a New Username')
        self.Request_Confirmation_Code = Request_Confirmation_Code(
            'Recovery Username'
        )
        self.users_db = Usuarios()
        self.auth_code = Get_Auth_Code()
        self.responses = Responses()
        self.verify = Verifications()
        self.Send_Email.clicked.connect(self.next_window)

    def get_user_email(self) -> list:
        return [self.Email.text().strip()]

    def next_window(self):

        email = self.get_user_email()

        if self.verify.empty_fields(email):
            self.responses.raise_alert(self.Response,
                                       'None of the fields can be empty.')
            return

        if self.verify.special_characters(email[0]):
            self.responses.raise_alert(self.Response,
                                       'There must not be special'
                                       'characters. '
                                       "(! # $ % ¨ & * + ')")
            return

        if not self.users_db.get_user_id(email[0]):
            self.responses.raise_error(self.Response, 'Invalid Password.')
            return

        if not self.verify.is_email(email[0]):
            self.responses.raise_error(self.Response, 'Invalid E-mail.')
            return

        SendEmail(self.auth_code, email[0]).send_email()
        self.Request_Confirmation_Code.show()
        self.responses.clear([self.Email], self.Response)
        self.close()
