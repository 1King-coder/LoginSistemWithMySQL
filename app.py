from sys import argv
from Login_sys.login_sys_code import Login_System
from PyQt5.QtWidgets import QApplication

qt = QApplication(argv)

system = Login_System()


system.show()
qt.exec_()
