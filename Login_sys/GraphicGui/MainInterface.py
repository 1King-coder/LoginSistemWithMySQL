# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 337)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Login)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.Login)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.Login)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 1, 1, 2)
        self.Password_login = QtWidgets.QLineEdit(self.Login)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Password_login.setFont(font)
        self.Password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_login.setObjectName("Password_login")
        self.gridLayout_2.addWidget(self.Password_login, 4, 1, 1, 2)
        self.User_email_login = QtWidgets.QLineEdit(self.Login)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.User_email_login.setFont(font)
        self.User_email_login.setObjectName("User_email_login")
        self.gridLayout_2.addWidget(self.User_email_login, 2, 1, 1, 2)
        self.Login_btn = QtWidgets.QPushButton(self.Login)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Login_btn.setFont(font)
        self.Login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Login_btn.setObjectName("Login_btn")
        self.gridLayout_2.addWidget(self.Login_btn, 5, 1, 1, 2)
        self.Forgot_pass = QtWidgets.QCommandLinkButton(self.Login)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Forgot_pass.setFont(font)
        self.Forgot_pass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Forgot_pass.setAutoRepeat(False)
        self.Forgot_pass.setObjectName("Forgot_pass")
        self.gridLayout_2.addWidget(self.Forgot_pass, 6, 1, 1, 1)
        self.Forgot_user = QtWidgets.QCommandLinkButton(self.Login)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Forgot_user.setFont(font)
        self.Forgot_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Forgot_user.setObjectName("Forgot_user")
        self.gridLayout_2.addWidget(self.Forgot_user, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 3, 1, 1)
        self.Login_response = QtWidgets.QLabel(self.Login)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.Login_response.setFont(font)
        self.Login_response.setText("")
        self.Login_response.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_response.setObjectName("Login_response")
        self.gridLayout_2.addWidget(self.Login_response, 7, 1, 1, 2)
        self.tabWidget.addTab(self.Login, "")
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Register)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.Email_regist = QtWidgets.QLineEdit(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Email_regist.setFont(font)
        self.Email_regist.setObjectName("Email_regist")
        self.gridLayout_3.addWidget(self.Email_regist, 4, 0, 1, 1)
        self.Username_regist = QtWidgets.QLineEdit(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Username_regist.setFont(font)
        self.Username_regist.setObjectName("Username_regist")
        self.gridLayout_3.addWidget(self.Username_regist, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 1)
        self.Register_btn = QtWidgets.QPushButton(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Register_btn.setFont(font)
        self.Register_btn.setObjectName("Register_btn")
        self.gridLayout_3.addWidget(self.Register_btn, 7, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 9, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.Password_regist = QtWidgets.QLineEdit(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Password_regist.setFont(font)
        self.Password_regist.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_regist.setObjectName("Password_regist")
        self.gridLayout_3.addWidget(self.Password_regist, 6, 0, 1, 1)
        self.Register_response = QtWidgets.QLabel(self.Register)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Register_response.setFont(font)
        self.Register_response.setText("")
        self.Register_response.setAlignment(QtCore.Qt.AlignCenter)
        self.Register_response.setObjectName("Register_response")
        self.gridLayout_3.addWidget(self.Register_response, 8, 0, 1, 1)
        self.tabWidget.addTab(self.Register, "")
        self.People_data = QtWidgets.QWidget()
        self.People_data.setObjectName("People_data")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.People_data)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Delete_btn = QtWidgets.QPushButton(self.People_data)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Delete_btn.setFont(font)
        self.Delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_btn.setStyleSheet("*{color: red;}")
        self.Delete_btn.setObjectName("Delete_btn")
        self.gridLayout_4.addWidget(self.Delete_btn, 3, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 3, 0, 1, 1)
        self.Database_people = QtWidgets.QTableWidget(self.People_data)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Database_people.setFont(font)
        self.Database_people.setObjectName("Database_people")
        self.Database_people.setColumnCount(4)
        self.Database_people.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(207, 203, 210))
        self.Database_people.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(207, 203, 210))
        self.Database_people.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(207, 203, 210))
        self.Database_people.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(207, 203, 210))
        self.Database_people.setHorizontalHeaderItem(3, item)
        self.gridLayout_4.addWidget(self.Database_people, 1, 0, 1, 3)
        self.Refresh_btn = QtWidgets.QPushButton(self.People_data)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Refresh_btn.setFont(font)
        self.Refresh_btn.setStyleSheet("*{color: blue;}")
        self.Refresh_btn.setObjectName("Refresh_btn")
        self.gridLayout_4.addWidget(self.Refresh_btn, 3, 1, 1, 1)
        self.tabWidget.addTab(self.People_data, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.User_email_login, self.Password_login)
        MainWindow.setTabOrder(self.Password_login, self.Login_btn)
        MainWindow.setTabOrder(self.Login_btn, self.Forgot_pass)
        MainWindow.setTabOrder(self.Forgot_pass, self.Forgot_user)
        MainWindow.setTabOrder(self.Forgot_user, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.Username_regist)
        MainWindow.setTabOrder(self.Username_regist, self.Email_regist)
        MainWindow.setTabOrder(self.Email_regist, self.Password_regist)
        MainWindow.setTabOrder(self.Password_regist, self.Register_btn)
        MainWindow.setTabOrder(self.Register_btn, self.Database_people)
        MainWindow.setTabOrder(self.Database_people, self.Refresh_btn)
        MainWindow.setTabOrder(self.Refresh_btn, self.Delete_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Username or E-mail:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.Login_btn.setText(_translate("MainWindow", "Log in"))
        self.Forgot_pass.setText(_translate("MainWindow", "I forgot my password"))
        self.Forgot_user.setText(_translate("MainWindow", "I forgot my Username"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Login), _translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.label_4.setText(_translate("MainWindow", "E-mail:"))
        self.label.setText(_translate("MainWindow", "Password:"))
        self.Register_btn.setText(_translate("MainWindow", "Register"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Register), _translate("MainWindow", "Register"))
        self.Delete_btn.setText(_translate("MainWindow", "Delete"))
        item = self.Database_people.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.Database_people.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "username"))
        item = self.Database_people.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "email"))
        item = self.Database_people.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "password"))
        self.Refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.People_data), _translate("MainWindow", "Registered people"))
