from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGridLayout, QLabel

'''
    Implementazionde della classe Ui_Centralina
    Crea la gui della vista di una centralina
'''

class Ui_Centralina():

    '''
        Costruisce la gui
    '''

    def setup_ui(self,ui):
       ui.setObjectName("sensori_frame")
       param_layout = QGridLayout()
       
       label1, label2, label3 = QLabel(""), QLabel(""), QLabel("")
       
       size = 200
       temp_img = QPixmap("img/temp.png").scaled(size,size,Qt.KeepAspectRatio,Qt.SmoothTransformation) 
       humid_img = QPixmap("img/humid.png").scaled(size,size,Qt.KeepAspectRatio,Qt.SmoothTransformation) 
       co2_img = QPixmap("img/co2.png").scaled(size,size,Qt.KeepAspectRatio,Qt.SmoothTransformation)

       label1.setScaledContents(True)
       label1.setFixedSize(40,40)
       label2.setScaledContents(True)
       label2.setFixedSize(40,40)
       label3.setScaledContents(True)
       label3.setFixedSize(40,40)
       
       label1.setPixmap(temp_img)
       label2.setPixmap(humid_img)
       label3.setPixmap(co2_img)

       label4, label5, label6 = QLabel("°C"), QLabel("%"), QLabel("ppm")
       self.temp_label = QLabel("")
       self.umid_label = QLabel("")
       self.co2_label = QLabel("")
       
       labels = [label1, label2, label3, label4, label5, label6, self.temp_label, self.umid_label, self.co2_label]

       for l in labels:
           l.setObjectName("centralina_param")
       
       param_layout.addWidget(label1,0,0)
       param_layout.addWidget(label2,1,0)
       param_layout.addWidget(label3,2,0)
       param_layout.addWidget(self.temp_label,0,1)
       param_layout.addWidget(self.umid_label,1,1)
       param_layout.addWidget(self.co2_label,2,1)
       param_layout.addWidget(label4,0,2)
       param_layout.addWidget(label5,1,2)
       param_layout.addWidget(label6,2,2)

       param_layout.setColumnStretch(0,2)
       param_layout.setColumnStretch(1,1)
       param_layout.setColumnStretch(2,1)

       ui.setLayout(param_layout)