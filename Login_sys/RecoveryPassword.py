from sys import argv
from .Data_base.Data_base import Usuarios
from .GraphicGui.RecoveryUsernameInterface import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from .Verifications_and_Responses.Verifications import Verifications
from .Verifications_and_Responses.Responses import Responses


class Recovery_Password(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
