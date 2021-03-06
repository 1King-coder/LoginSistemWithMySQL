from .SendEmail import SendEmail
from .Data_base.Data_base import Usuarios
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .RequestConfirmationCode import Request_Confirmation_Code
from .SendCode.GenerateAuthCode import Get_Auth_Code
from .SendCode.Cache import Cache
from .GraphicGui.RequestNewPasswordInterface import *


class Request_New_Password(QMainWindow, Ui_MainWindow):
    """
    Class responsible for sending the authentication
    code to access the recovery password window
    where the user will be able to change his password.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowTitle('Request a New Password')
        self.Request_Confirmation_Code = Request_Confirmation_Code(
            'Recovery Password')
        self.users_db = Usuarios()
        self.responses = Responses()
        self.verify = Verifications()
        self.Confirm.clicked.connect(self.confirm)

    def get_user_input(self):
        return [self.User_input.displayText()]

    def confirm(self):
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

        """Try to get the user's input id."""
        if not self.users_db.get_user_id(user_input[0]):
            self.responses.raise_error(self.Response,
                                       'Invalid Username or E-mail.')
            return

        """Stores momentaly the user's input for Recovery Password."""
        Cache(user_input[0])

        """Get the Auth code and send it by the user's email."""
        SendEmail(Get_Auth_Code(), user_input[0]).send_email()

        """Open the Authentication window."""
        self.Request_Confirmation_Code.show()

        """Clear the inputs and responser."""
        self.responses.clear([self.User_input], self.Response)
        self.close()
