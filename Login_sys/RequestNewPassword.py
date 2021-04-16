from .SendEmail import SendEmail
from .Data_base.Data_base import Usuarios
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .RequestConfirmationCode import Request_Confirmation_Code
from .SendCode.GenerateAuthCode import Get_Auth_Code
from .GraphicGui.RequestNewPasswordInterface import *


class Request_New_Password(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.Request_Confirmation_Code = Request_Confirmation_Code()
        self.users_db = Usuarios()
        self.auth_code = Get_Auth_Code()
        self.responses = Responses()
        self.verify = Verifications()
        self.Confirm.clicked.connect(self.next_window)

    def get_user_input(self):
        return [self.User_input.displayText()]

    def next_window(self):
        user_input = self.get_user_input()

        if self.verify.empty_fields(user_input):
            self.responses.raise_alert(self.Response,
                                       'None of the fields can be empty.')
            return

        if self.verify.special_characters(user_input[0]):
            self.responses.raise_alert(self.Response,
                                       'There must not be special'
                                       'characters. '
                                       "(! # $ % ¨ & * + ')")
            return

        if not self.users_db.get_user_id(user_input[0]):
            self.responses.raise_error(self.Response,
                                       'Invalid Username or E-mail.')
            return

        SendEmail(self.auth_code, user_input[0]).send_email()
        self.Request_Confirmation_Code.show()
        self.responses.clear(self.Response, [self.User_input])
        self.close()
