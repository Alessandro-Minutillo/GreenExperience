from PyQt5.QtCore import Qt
from serra.view.vista_serra import Vista_Serra
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QFrame

'''
    Implementazione della classe Ui_Home
    Crea la gui della vista home
'''

class Ui_Home():

    '''
        Crea la gui
    '''

    def setup_ui(self,ui):
        self.hlayout = QHBoxLayout()
        self.frame_panel = QFrame()
        self.frame_panel.setObjectName("frame_panel")
        self.panel = QVBoxLayout()

        self.profile_layout = QVBoxLayout()
        pic_layout = QHBoxLayout()
        
        self.profile_pic = QLabel()
        self.profile_pic.setAlignment(Qt.AlignCenter)
        self.profile_pic.setScaledContents(True)
        self.profile_pic.setFixedSize(150,150)

        pic_layout.addStretch()
        pic_layout.addWidget(self.profile_pic)
        pic_layout.addStretch()

        self.profile_label = QLabel()
        self.profile_label.setAlignment(Qt.AlignCenter)
        
        self.profile_layout.addLayout(pic_layout)
        self.profile_layout.addWidget(self.profile_label)
        self.profile_layout.setStretch(0,3)
        self.profile_layout.setStretch(1,1)

        self.menu_box = QGroupBox("Menu")
        self.menu_layout = QVBoxLayout()
        self.menu_box.setObjectName("menu")
        
        self.button = []

        for i, string in enumerate(["Account", "Notifiche", "Database Colture","Produttività","Consumi"]):
            self.button.append(QPushButton(string))
        
        self.menu_layout.addWidget(self.button[0])
        self.menu_layout.addWidget(self.button[1])
        self.menu_layout.addWidget(self.button[2])
        self.menu_box.setLayout(self.menu_layout)

        self.dashboard_box = QGroupBox("Dashboard")
        self.dashboard_box.setObjectName("menu")
        self.dashboard_layout = QVBoxLayout()
        self.dashboard_layout.addWidget(self.button[3])
        self.dashboard_layout.addWidget(self.button[4])
        self.dashboard_box.setLayout(self.dashboard_layout)

        self.cambia_button = QPushButton("Cambia utente")
        
        self.panel.addLayout(self.profile_layout)
        self.panel.addStretch()
        self.panel.addWidget(self.menu_box)
        self.panel.addStretch()
        self.panel.addWidget(self.dashboard_box)
        self.panel.addStretch()
        self.panel.addWidget(self.cambia_button)
        
        option_stretch = [6,1,6,1,4,2,3]
        
        for i,s in enumerate(option_stretch):
            self.panel.setStretch(i,s)
        
        self.frame_panel.setLayout(self.panel)
        self.vlayout = QVBoxLayout()
        
        self.data_layout = QHBoxLayout()
        self.data_layout.addStretch()
        self.data_label = QLabel("qui data")
        self.data_label.setObjectName("data_label")
        self.data_layout.addWidget(self.data_label)
        
        data_stretch = [10,1]

        for i, s in enumerate(data_stretch):
            self.data_layout.setStretch(i,s)
        
        self.vlayout.addLayout(self.data_layout)
        self.serra_frame = Vista_Serra(ui,ui.main_window)
        self.vlayout.addWidget(self.serra_frame)
        vlayout_stretch = [1,20]

        for i, s in enumerate(vlayout_stretch):
            self.vlayout.setStretch(i,s)

        self.hlayout.addWidget(self.frame_panel)
        self.hlayout.addLayout(self.vlayout)
        
        hlayout_stretch = [1,3]

        for i, s in zip(range(len(hlayout_stretch)),hlayout_stretch):
            self.hlayout.setStretch(i,s)

        ui.setLayout(self.hlayout)
        return self