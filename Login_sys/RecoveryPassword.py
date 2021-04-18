from .Data_base.Data_base import Usuarios
from .GraphicGui.RecoveryPasswordInterface import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses
from .SendCode.Cache import Cache


class Recovery_Password(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowTitle('Change Password')
        self.users_db = Usuarios()
        self.responses = Responses()
        self.cache = Cache()
        self.verify = Verifications()
        self.Change_btn.clicked.connect(self.change_password_in_db)

    def get_user_inputs(self) -> list:
        return [
            self.New_pass.text(),
            self.New_pass_repeat.text()
        ]

    def change_password_in_db(self):
        new_passwords = self.get_user_inputs()

        if self.verify.empty_fields(new_passwords):
            self.responses.raise_alert(self.Response,
                                       'None of the fields can be empty.')
            return

        """Compare the passwords."""
        if new_passwords[0] != new_passwords[1]:
            self.responses.raise_error(self.Response,
                                       'Passwords do not match.')
            return

        try:
            """
            Try to change the password in the DB
            using the user input inserted in the
            request new password class with the 
            cache's class function.
            """
            if not self.users_db.change_password(str(self.cache()),
                                                 new_passwords[1]):
                self.responses.raise_error(self.Response,
                                           'An error has occurred.')
                return
            self.responses.success_message(self.Response,
                                           'Password succesfully changed!')

            Cache('')  # Clear the Cache.

        except Exception:
            self.responses.raise_error(self.Response,
                                       'An error has occurred while '
                                       'trying to change password '
                                       'in DataBase.')

        self.responses.clear([self.New_pass, self.New_pass_repeat],
                             self.Response)
