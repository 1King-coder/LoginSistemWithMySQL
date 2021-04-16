from sys import argv
from .Data_base.Data_base import Usuarios
from .GraphicGui.RecoveryUsernameInterface import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses


class Recovery_Username(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.users_db = Usuarios()
        self.responses = Responses()
        self.verify = Verifications()
        self.Change_btn.clicked.connect(self.change_username_in_db)

    def get_user_inputs(self):
        return [
            self.New_username.displayText(),
            str(self.Password.text())
        ]

    def change_username_in_db(self):
        user_inputs = self.get_user_inputs()

        if self.verify.empty_fields(user_inputs):
            self.responses.raise_alert(self.Response,
                                       'None of the fields can be empty.')
            return

        if self.verify.is_email(user_inputs[0]):
            self.responses.raise_error(self.Response,
                                       'New username cannot be a e-mail.')
            return

        if self.verify.special_characters(user_inputs[0]):
            self.responses.raise_alert(self.Response,
                                       'There must not be special'
                                       'characters. '
                                       "(! # $ % ¨ & * + ')")
            return

        if self.users_db.verify_if_user_is_registered(user_inputs[0]):
            self.responses.raise_alert(self.Response,
                                       'Username already taken.')
            return

        try:
            if not self.users_db.change_username(user_inputs[0],
                                                 user_inputs[1]):
                self.responses.raise_error(self.Response,
                                           'Invalid Password')
                return
            self.responses.success_message(self.Response,
                                           'Username succesfully changed!')
        except Exception:
            self.responses.raise_error(self.Response,
                                       'An error has occurred while '
                                       'trying to change username '
                                       'in DataBase.')
