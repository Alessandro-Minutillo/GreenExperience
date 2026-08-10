from PyQt5 import QtCore, QtGui, QtWidgets

'''
    Implementazione della classe Ui_Login
    Crea la gui della vista login
'''

class Ui_Login():
    
    '''
        Crea la gui
    '''

    def setup_ui(self, ui):
        ui.setObjectName("ui")
        ui.resize(960, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(ui)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.logo_label = QtWidgets.QLabel(ui)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout.addWidget(self.logo_label)
        logo_layout = QtWidgets.QHBoxLayout()
        self.logo_img = QtWidgets.QLabel()
        self.logo_img.setFixedSize(256,256)
        self.logo_img.setScaledContents(True)
        logo_layout.addStretch()
        logo_layout.addWidget(self.logo_img)
        logo_layout.addStretch()
        self.verticalLayout.addLayout(logo_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.login_label = QtWidgets.QLabel(ui)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.verticalLayout.addWidget(self.login_label)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        
        #label errore username e password
        self.error_label = QtWidgets.QLabel(ui)
        self.error_label.setObjectName("error_label")
        self.verticalLayout2.addWidget(self.error_label)

        #campo username
        self.edit_username = QtWidgets.QLineEdit(ui)
        self.edit_username.setObjectName("lineEdit")
        self.edit_username.setPlaceholderText("username")
        self.verticalLayout2.addWidget(self.edit_username)
        
        #campo password
        self.edit_password = QtWidgets.QLineEdit(ui)
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.edit_password.setPlaceholderText("password")
        self.verticalLayout2.addWidget(self.edit_password)
        
        self.horizontalLayout.addLayout(self.verticalLayout2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)

        #button "Accedi come admin"
        self.adminbutton = QtWidgets.QPushButton(ui)
        self.adminbutton.setAutoDefault(True)
        self.adminbutton.setObjectName("adminbutton")
        
        self.horizontalLayout_2.addWidget(self.adminbutton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.oppure = QtWidgets.QLabel(ui)
        self.oppure.setAlignment(QtCore.Qt.AlignCenter)
        self.oppure.setObjectName("oppure")
        self.verticalLayout.addWidget(self.oppure)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        
        #button "Accedi come guest"
        self.guestbutton = QtWidgets.QPushButton(ui)
        self.guestbutton.setObjectName("guestbutton")
        
        self.horizontalLayout_3.addWidget(self.guestbutton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)

        self.retranslateUi(ui)
        QtCore.QMetaObject.connectSlotsByName(ui)

    '''
        Setta i testi della view
    '''

    def retranslateUi(self, ui):
        _translate = QtCore.QCoreApplication.translate
        ui.setWindowTitle(_translate("ui", "Login"))
        self.logo_label.setText(_translate("ui", "Green Experience"))
        self.login_label.setText(_translate("ui", "Login"))
        logo = QtGui.QPixmap("img/logo_senza_sfondo.png").scaled(512,512,
                                                            QtCore.Qt.KeepAspectRatio,
                                                            QtCore.Qt.SmoothTransformation)
        self.logo_img.setPixmap(logo)
        self.adminbutton.setText(_translate("ui", "Accedi come admin"))
        self.oppure.setText(_translate("ui", "oppure"))
        self.guestbutton.setText(_translate("ui", "Accedi come ospite"))