from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel, QVBoxLayout
from qtwidgets.toggle.toggle import AnimatedToggle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

'''
    Implementazione della classe Ui_Luce
    Implementa la gui della vista dell'impianto di illuminazione
'''

class Ui_Luce_Reg():
    
    '''
        Costruisce la gui
        Parametri:
            (attuatore_generico.luce_reg.view.vista_luce_reg) ui, vista dell'impianto di illuminazione
    '''

    def setup_ui(self,ui):
       ui.setObjectName("frame_luci")
       
       #layout esterno
       layout = QVBoxLayout()
       
       #barra
       bar = QHBoxLayout()
       
       self.onoff_luci = AnimatedToggle(checked_color="#00ff00" ,pulse_checked_color = "#00ff00")
       
       label = QLabel("Impianto illuminazione")
       label.setObjectName("nome_att")
       label.setAlignment(Qt.AlignCenter)
       
       bar.addWidget(self.onoff_luci)
       bar.addStretch()
       bar.addWidget(label)
       img_label = QLabel()
       img_label.setScaledContents(True)
       img_label.setFixedSize(66,66)
       img = QPixmap("img/lamp.png").scaled(200, 200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
       img_label.setPixmap(img)
       bar.addStretch()
       bar.addWidget(img_label)
       
       stretch = [1, 1, 3, 1, 1]
       for i,s in enumerate(stretch):
           bar.setStretch(i,s)

       setting = QHBoxLayout()
       
       label2 = QLabel("Tipo luce")
       label2.setFont(QFont("Arial",12))
       self.combo_luce = QComboBox()
       
       for type in ["rossa", "infrarossi", "blu", "ultravioletto"]:
           self.combo_luce.addItem(type)

       setting.addWidget(label2)
       setting.addWidget(self.combo_luce)
       
       stretch = [1, 2]
       for i,s in enumerate(stretch):
           setting.setStretch(i,s)
       
       layout.addLayout(bar)
       layout.addLayout(setting)

       stretch = [1, 2]
       for i,s in enumerate(stretch):
           layout.setStretch(i,s)

       ui.setLayout(layout) 