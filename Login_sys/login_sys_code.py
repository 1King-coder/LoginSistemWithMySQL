from sys import argv
from .GraphicGui.MainInterface import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from .Data_base.Data_base import Usuarios
from .RequestNewUsername import Request_New_Username
from .RequestNewPassword import Request_New_Password
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses


class Login_System(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.responses = Responses()
        self.verify = Verifications()
        self.Request_New_Username = Request_New_Username()
        self.Request_New_Password = Request_New_Password()
        self.users_db = Usuarios()
        self.show_registered_people()
        self.setWindowTitle('Login System from Vitor')
        self.Login_btn.clicked.connect(self.log_in_system)
        self.Register_btn.clicked.connect(self.register)
        self.Forgot_pass.clicked.connect(self.recover_password)
        self.Forgot_user.clicked.connect(self.recover_user)
        self.Refresh_btn.clicked.connect(self.show_registered_people)
        self.Delete_btn.clicked.connect(self.delete_from_database)

    def get_user_regis_input(self) -> list:
        return [
            self.Username_regist.displayText().strip(),
            self.Email_regist.displayText().strip(),
            self.Password_regist.text().strip()
        ]

    def get_user_login_input(self) -> list:
        return [
            self.User_email_login.displayText().strip(),
            self.Password_login.text().strip()
        ]

    def insert_into_database(self, username, email, password):
        self.users_db.register_new_user(
            username, email, password)
        Responses.success_message(self.Register_response,
                                  f'User: {username} succesfully registered')

    def log_in_system(self):
        try:
            user_login_inputs = self.get_user_login_input()
            confirm_inputs = self.users_db.confirm_login(
                user_login_inputs[0],
                user_login_inputs[1])
        except Exception:
            self.responses.raise_error(self.Login_response,
                                       'An Error has occurred '
                                       'while trying to login')

        if self.verify.empty_fields(user_login_inputs):
            self.responses.raise_alert(self.Login_response,
                                       'None of the fields can be empty.')
            return

        if confirm_inputs == 'Confirm':

            self.responses.success_message(self.Login_response,
                                           'Successfuly Logged!')

        elif confirm_inputs == 'Invalid password':
            self.responses.raise_error(self.Login_response, confirm_inputs)

        else:
            self.responses.raise_alert(self.Login_response,
                                       'User not registered in the system')

    def register(self):

        user_regist_inputs = self.get_user_regis_input()

        if self.verify.empty_fields(user_regist_inputs):
            self.responses.raise_alert(self.Register_response,
                                       'None of the fields can be empty.')
            return

        if self.verify.special_characters(user_regist_inputs):
            self.responses.raise_alert(self.Register_response,
                                       'There must not be special'
                                       'characters.'
                                       "(! # $ % ¨ & * + ')")
            return

        if self.users_db.verify_if_user_is_registered(
                user_regist_inputs[0]):
            self.responses.raise_alert(self.Register_response,
                                       f'User: {user_regist_inputs[0]}'
                                       ' Already registered')
            return

        try:
            self.insert_into_database(
                user_regist_inputs[0], user_regist_inputs[1],
                user_regist_inputs[2])

        except Exception:
            self.responses.raise_error(self.Register_response,
                                       'An Error has occurred '
                                       'while trying '
                                       'to register user.')

    def show_registered_people(self):
        table_row = 0
        try:
            people_data = self.users_db.list_registered_users()
            self.Database_people.setRowCount(len(people_data))
            for row in people_data:
                self.Database_people.setItem(
                    table_row, 0, QTableWidgetItem(row['id']))
                self.Database_people.setItem(
                    table_row, 1, QTableWidgetItem(row['username']))
                self.Database_people.setItem(
                    table_row, 2, QTableWidgetItem(row['email']))
                self.Database_people.setItem(
                    table_row, 3, QTableWidgetItem(row['password_hash']))
                table_row += 1
        except Exception:
            self.Database_people.setRowCount(1)
            self.Database_people.setItem(0, 0, 'An error has occurred '
                                         'while trying to retrieve Data.')

    def recover_password(self):
        pass

    def recover_user(self):
        self.Request_New_Username.show()

    def delete_from_database(self):
        pass
