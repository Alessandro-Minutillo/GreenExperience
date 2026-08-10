from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import QFrame, QGridLayout, QProgressBar, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox
from attuatore_generico.luce_reg.view.vista_luce_reg import Vista_Luce_Reg
from centralina.view.vista_centralina import Vista_Centralina

'''
    Implementazione della classe Ui_Lotto
    Crea la gui della vista lotto
'''

class Ui_Lotto():
    
    '''
        Costruisce il frame del lotto
    '''

    def build_frame_lotto_sing(self,obj, name, text, id):
       obj.setObjectName(name)
       obj.setProperty("class","lotti")
       obj.setScaledContents(True)      
       layout = QVBoxLayout()
       self.lotto_text_label = QLabel()
       self.lotto_text_label.setObjectName("etichetta_lotto")
       self.lotto_text_label.setAlignment(Qt.AlignCenter)
       layout.addWidget(self.lotto_text_label)
       obj.setLayout(layout)
       
       self.sensori_frame = Vista_Centralina(id)
       self.sensori_frame.setParent(obj)
       self.sensori_frame.setFixedSize(QSize(166,166))
       pos = QPoint(0,0)
       self.sensori_frame.move(pos)

    '''
        Costruisce il frame con le informazioni relative al lotto
    '''

    def build_frame_info(self,obj, name, text):
       obj.setObjectName(name)
       layout = QVBoxLayout()
       
       box1 = QGroupBox("Status lotto")
       self.status_bar = QProgressBar()
       self.status_bar.setObjectName("status_bar")
       self.status_bar.setTextVisible(False)

       param_layout = QGridLayout()
       
       label0, label1, label2, label3 = QLabel("Salute: "),QLabel("Fase fenologica corrente: "), QLabel("Luce consigliata: "), QLabel("Stato: ")
       
       self.fase_label = QLabel("x")
       self.luce_label = QLabel("x")
       self.stato_label = QLabel("x")

       param_layout.addWidget(label3,0,0)
       param_layout.addWidget(label0,1,0)
       param_layout.addWidget(label1,2,0)
       param_layout.addWidget(label2,3,0)
       param_layout.addWidget(self.stato_label,0,1)
       param_layout.addWidget(self.status_bar,1,1)
       param_layout.addWidget(self.fase_label,2,1)
       param_layout.addWidget(self.luce_label,3,1)
       
       param_layout.setColumnStretch(0,1)
       param_layout.setColumnStretch(1,2)
       
       box1.setLayout(param_layout)
       
       box2 = QGroupBox("Statistiche lotto")
       box2_layout = QGridLayout()

       label3, label4 = QLabel("Data inizio coltivazione: "), QLabel("Data fine coltivazione: ")
       self.inizio_label = QLabel("x")
       self.fine_label = QLabel("x")
       
       box2_layout.addWidget(label3,0,0)
       box2_layout.addWidget(label4,1,0)
       box2_layout.addWidget(self.inizio_label,0,1)
       box2_layout.addWidget(self.fine_label,1,1)
       
       box2_layout.setColumnStretch(0,1)
       box2_layout.setColumnStretch(1,1)

       box2.setLayout(box2_layout)

       box3 = QGroupBox("Note sul lotto")
       box3_layout = QHBoxLayout()
       self.note_edit = QTextEdit()
       box3_layout.addWidget(self.note_edit)
       box3.setLayout(box3_layout)

       for box in [box1, box2, box3]:
           box.setObjectName("box")

       layout.addWidget(box1)
       layout.addWidget(box2)
       layout.addWidget(box3)
       stretch = [3,2,3]
       for i,s in enumerate(stretch):
           layout.setStretch(i,s)
       obj.setLayout(layout)


    '''
        Crea la gui
    '''

    def setup_ui(self,ui):
       
       ui.setObjectName("settore")
       self.main_container = QVBoxLayout()
       
       hlayout0 = QHBoxLayout()
       hlayout0.addStretch()
       self.data_label = QLabel("qui data")
       self.data_label.setObjectName("data_label")
       hlayout0.addWidget(self.data_label)
       hlayout0.setStretch(0,15)
       hlayout0.setStretch(1,1)

       hlayout1 = QHBoxLayout()
       hlayout1.setSpacing(20)

       self.frame_tot = QFrame()
       self.frame_tot.setObjectName("frame_tot")

       lotto_layout = QVBoxLayout()
       
       id_1 = ui.controller.get_luce_id()
       self.frame_luci = Vista_Luce_Reg(ui.parent_ui,ui.main_window,id_1)
       
       self.frame_lotto_sing = QLabel()
       id_2 = ui.controller.get_centralina_id()
       self.build_frame_lotto_sing(self.frame_lotto_sing,"frame_lotto_sing","Lotto",id_2)
       
       lotto_layout.addWidget(self.frame_luci)
       lotto_layout.addWidget(self.frame_lotto_sing)
       lotto_layout.setStretch(0,1)
       lotto_layout.setStretch(1,4)

       self.frame_tot.setLayout(lotto_layout)

       self.frame_info = QFrame()
       self.build_frame_info(self.frame_info,"frame_info","Info")

       hlayout1.addWidget(self.frame_tot)
       hlayout1.addWidget(self.frame_info)
       hlayout1.setStretch(0,3)
       hlayout1.setStretch(1,2)


       hlayout2 = QHBoxLayout()
       
       self.error_label = QLabel()
       self.error_label.setObjectName("error_label")
       self.indietro = QPushButton("indietro")
       self.button_raccogli = QPushButton("Raccogli")
       self.button_pianta = QPushButton("Pianta")
       
       hlayout2.addWidget(self.indietro)
       hlayout2.addStretch()
       hlayout2.addWidget(self.error_label)
       hlayout2.addStretch()
       hlayout2.addWidget(self.button_raccogli)
       hlayout2.addStretch()
       hlayout2.addWidget(self.button_pianta)
       hlayout2.setSpacing(10)

       stretch = [1, 2, 4, 2, 1, 3, 1]

       for i, s in enumerate(stretch):
            hlayout2.setStretch(i,s)

       self.main_container.addLayout(hlayout0)
       self.main_container.addLayout(hlayout1)
       self.main_container.addLayout(hlayout2)
       
       self.main_container.setStretch(0,1)
       self.main_container.setStretch(1,18)
       self.main_container.setStretch(2,1)

       ui.setLayout(self.main_container)