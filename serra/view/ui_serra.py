from PyQt5.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

'''
    Implementazione della classe Ui_Serra
    Crea la gui della vista serra
'''

class Ui_Serra():
    
    '''
        Crea la gui
    '''

    def setup_ui(self,ui):
       
       ui.setObjectName("serra")
       self.alert_label_serra = {}
       self.main_container = QHBoxLayout()
       self.frame_serra = QFrame()
       self.frame_serra.setObjectName("frame_serra")
       
       self.four_layout = QGridLayout()
       
       self.four_layout.setVerticalSpacing(5)
       self.four_layout.setHorizontalSpacing(10)

       rows, cols = 2, 2
       self.settori = []
       
       img = QPixmap("img/settore.png").scaled(400, 
                                                            200,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
       for i in range(rows):
            for j in range(cols):
                frame = QLabel()
                frame.setScaledContents(True)
                frame.setPixmap(img)
                frame.setObjectName("frame_settore")
                vlayout = QVBoxLayout()
                hlayout = QHBoxLayout()
                
                alert_label = QLabel("")
                alert_label.setObjectName("alert_label")
                alert_label.setScaledContents(True)
                alert_label.setFixedSize(66, 66)
                
                hlayout.addWidget(alert_label)
                hlayout.addStretch()
                hlayout.setStretch(0,1)
                hlayout.setStretch(1,10)

                label = QLabel("")
                label.setObjectName("nome_settore")
                label.setAlignment(Qt.AlignCenter)
                
                vlayout.addLayout(hlayout)
                vlayout.addWidget(label)
                
                vlayout.setStretch(0,1)
                vlayout.setStretch(1,6)

                frame.setLayout(vlayout)
                self.settori.append(frame)
                self.four_layout.addWidget(frame,i,j)
       
       self.frame_serra.setLayout(self.four_layout)
       self.main_container.addWidget(self.frame_serra)
       ui.setLayout(self.main_container)