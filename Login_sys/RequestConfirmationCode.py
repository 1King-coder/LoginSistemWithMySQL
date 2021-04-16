from random import randint
from .Data_base.Data_base import Usuarios
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .GraphicGui.RequestConfirmationCodeInterface import *
from .RecoveryPassword import Recovery_Password
from .SendCode.GenerateAuthCode import Get_Auth_Code
from .SendCode.Cache import Cache


class Request_Confirmation_Code(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.Recovery_Password = Recovery_Password()
        self.auth_code = Get_Auth_Code()
        self.users_db = Usuarios()
        self.responses = Responses()
        self.verify = Verifications()
        self.Confirm_btn.clicked.connect(self.next_window)

    def next_window(self):
        user_input = [self.Code.displayText()]

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

        if not user_input[0] == str(self.auth_code):
            self.responses.raise_error(self.Response,
                                       'Incorrect Code.')
            return

        self.Recovery_Password.show()
        self.responses.clear(self.Response, [self.Code])
        self.close()
        print(Cache())
