from random import randint
from .Data_base.Data_base import Usuarios
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .GraphicGui.RequestConfirmationCodeInterface import *
from .RecoveryPassword import Recovery_Password
from .RecoveryUsername import Recovery_Username
from .SendCode.GenerateAuthCode import Get_Auth_Code
from .SendCode.Cache import Cache
from time import sleep


class Request_Confirmation_Code(QMainWindow, Ui_MainWindow):
    """
    Class responsible for validating the authentication
    code and lead for the correspondent data revocery.
    """

    def __init__(self, flag, parent=None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.setWindowTitle('Authentication')
        self.flag = flag

        """Initialize the Recovery_Password or Recovery_Username classes."""
        if self.flag == 'Recovery Password':
            self.Recovery_Password = Recovery_Password()
        else:
            self.Recovery_Username = Recovery_Username()

        """Retrieve the Auth code sended by e-mail"""
        self.auth_code = Get_Auth_Code(None)
        self.cache = Cache()
        self.users_db = Usuarios()
        self.responses = Responses()
        self.verify = Verifications()
        self.Confirm_btn.clicked.connect(self.validate)

    def get_user_input(self) -> list:
        return [self.Code.displayText()]

    def validate(self):
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

        """Validate the auth code"""
        if not user_input[0] == str(self.auth_code):
            self.responses.raise_error(self.Response,
                                       'Incorrect Code.')
            return

        """Clear input and responser"""
        self.responses.clear([self.Code], self.Response)

        if self.flag == 'Recovery Password':
            """Open Recovery Password window."""
            self.Recovery_Password.show()

            self.close()

        if self.flag == 'Recovery Username':
            """Open Recovery Username window."""
            self.Recovery_Username.show()

            self.close()

        """Generate a new auth code for a next usage."""
        Get_Auth_Code(True)
