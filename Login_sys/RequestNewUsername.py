from sys import argv
from .Data_base.Data_base import Usuarios
from .GraphicGui.RequestNewUsernameInterface import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .RecoveryUsername import Recovery_Username


class Request_New_Username(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.Recovery_Username = Recovery_Username()
        self.users_db = Usuarios()
        self.responses = Responses()
        self.verify = Verifications()
        self.Send_Email.clicked.connect(self.next_window)

    def next_window(self):

        password = [self.Password.text().strip()]

        if self.verify.empty_fields(password):
            self.responses.raise_alert(self.Response,
                                       'None of the fields can be empty.')
            return

        if self.verify.special_characters(password[0]):
            self.responses.raise_alert(self.Response,
                                       'There must not be special'
                                       'characters. '
                                       "(! # $ % ¨ & * + ')")
            return

        if not self.users_db.get_user_id_by_pass(password[0]):
            self.responses.raise_error(self.Response, 'Invalid Password')
            return

        self.Recovery_Username.show()
