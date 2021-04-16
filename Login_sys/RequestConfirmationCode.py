from random import randint
from .Data_base.Data_base import Usuarios
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .GraphicGui.RequestConfirmationCodeInterface import *
from .RecoveryPassword import Recovery_Password
from .SendCode.GenerateAuthCode import Get_Auth_Code
from .SendCode.Cache import Cache
from time import sleep


class Request_Confirmation_Code(QMainWindow, Ui_MainWindow):
    def __init__(self, flag, parent=None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.setWindowTitle('Authentication')
        self.flag = flag
        self.Recovery_Password = Recovery_Password()
        self.auth_code = Get_Auth_Code(None)
        self.cache = Cache()
        self.users_db = Usuarios()
        self.responses = Responses()
        self.verify = Verifications()
        self.Confirm_btn.clicked.connect(self.confirm)

    def confirm(self):
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

        if self.flag == 'Recovery Password':
            self.Recovery_Password.show()
            return

        if self.flag == 'Recovery Username':
            try:
                if not self.users_db.change_username(str(self.cache()[0]),
                                                     str(self.cache()[1])):

                    self.responses.raise_error(self.Response,
                                               'Invalid Email')
                    return

                self.responses.success_message(self.Response,
                                               'Username succesfully changed!')

                sleep(5)

            except Exception:
                self.responses.raise_error(self.Response,
                                           'An error has occurred while '
                                           'trying to change username '
                                           'in DataBase.')
                return

        Get_Auth_Code(True)
        self.responses.clear(self.Response, [self.Code])
        self.close()
        Cache('')
