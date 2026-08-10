from PyQt5.QtCore import Qt
from avvisi.view.vista_bacheca_att import Vista_Bacheca_Att
from avvisi.view.vista_bacheca_sl import Vista_Bacheca_SL
from avvisi.view.vista_bacheca_pr import Vista_Bacheca_PR
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel

'''
     Implementazione della classe Ui_Avvisi
     Crea la gui della vista avvisi
'''

class Ui_Avvisi():

    '''
     Costruisce la gui
     Parametri:
          (avvisi.view.vista_avvisi) ui, vista avvisi
    '''

    def setup_ui(self,ui):

       self.main_container = QVBoxLayout()
       
       hlayout0 = QHBoxLayout()
       hlayout0.addStretch()
       self.data_label = QLabel("qui data")
       self.data_label.setObjectName("data_label")
       hlayout0.addWidget(self.data_label)
       hlayout0.setStretch(0,15)
       hlayout0.setStretch(1,1)

       hlayout05 = QHBoxLayout()
       hlayout05.setSpacing(10)
       title_layout = QHBoxLayout()
       label = QLabel(" Notifiche")
       label.setObjectName("avvisi")
       img_label = QLabel()
       img_label.setFixedSize(80,80)
       img_label.setScaledContents(True)
       img = QPixmap("img/notify.png").scaled(100,100,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
       img_label.setPixmap(img)
       title_layout.addWidget(label)
       title_layout.addWidget(img_label)
       title_layout.addStretch()

       hlayout05.addLayout(title_layout)

       hlayout1 = QHBoxLayout()
       hlayout1.setSpacing(4)
       
       self.bacheca1 = Vista_Bacheca_PR(ui,ui.main_window)
       self.bacheca2 = Vista_Bacheca_SL(ui,ui.main_window)
       self.bacheca3 = Vista_Bacheca_Att(ui,ui.main_window)
       
       hlayout1.addWidget(self.bacheca1)
       hlayout1.addWidget(self.bacheca2)
       hlayout1.addWidget(self.bacheca3)
       hlayout1.setStretch(0,9)
       hlayout1.setStretch(1,10)
       hlayout1.setStretch(2,9)

       hlayout2 = QHBoxLayout()
       self.indietro = QPushButton("indietro")
       
       hlayout2.addWidget(self.indietro)
       hlayout2.addStretch()
       hlayout2.setSpacing(10)

       stretch = [1, 13]

       for i, s in enumerate(stretch):
            hlayout2.setStretch(i,s)

       self.main_container.addLayout(hlayout0)
       self.main_container.addLayout(hlayout05)
       self.main_container.addLayout(hlayout1)
       self.main_container.addLayout(hlayout2)
       
       self.main_container.setStretch(0,1)
       self.main_container.setStretch(1,2)
       self.main_container.setStretch(2,18)
       self.main_container.setStretch(3,1)

       ui.setLayout(self.main_container)