from PyQt5.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

'''
    Implementazione della classe Ui_Notifica
    Implementa la gui del widget che rappresenta una notifica
    nella vista bacheca
'''

class Ui_Notifica():
    
    '''
        Costruisce la gui
        Parametri:
            (avvisi.view.vista_notiifica) ui, vista_notifica
    '''

    def setup_ui(self,ui):
        main_container = QVBoxLayout()
        frame = QFrame()
        frame.setObjectName("notifica")

        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.hlayout2 = QHBoxLayout()
        
        self.img = QLabel()
        self.img.setScaledContents(True)
        self.img.setFixedSize(50,50)
        self.img.setPixmap(ui.icon)
        self.text = QLabel(ui.message)
        self.text.setObjectName("notifica")

        self.hlayout2.addStretch()
        self.buttons = []
        
        for msg in ui.button_messages:
            btn = QPushButton(msg)
            self.buttons.append(btn)
            self.hlayout2.addWidget(btn)

        vlayout.addWidget(self.text)
        vlayout.addLayout(self.hlayout2)
        
        hlayout.addWidget(self.img)
        hlayout.addLayout(vlayout)

        hlayout.setStretch(0,1)
        hlayout.setStretch(1,2)
        frame.setLayout(hlayout)
        
        main_container.addWidget(frame)
        ui.setLayout(main_container)