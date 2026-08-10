from colture.view.vista_selezione_coltura import Vista_Selezione_Coltura
from PyQt5.QtWidgets import QFrame, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtGui import QPixmap

'''
   Implementazione della classe Ui_Settore
   Crea la gui della vista settore
'''

class Ui_Settore():
    
    '''
      Costruisce il frame di un attuatore
    '''

    def build_frame_att(self,obj, name, text):
       obj.setObjectName(name)
       obj.setProperty("class","frame_att")
       
       layout = QVBoxLayout()

       label = QLabel(text)
       label.setObjectName("nome_att")
       label.setAlignment(Qt.AlignCenter)
       label.setAttribute(Qt.WA_TranslucentBackground)
       
       bar = QHBoxLayout()
       
       onoff_label = QLabel()
       onoff_label.setObjectName("onoff_label")
       onoff_label.setScaledContents(True)
       onoff_label.setFixedSize(40,40)
       
       alert_label = QLabel()
       alert_label.setObjectName("alert_label")
       alert_label.setScaledContents(True)
       alert_label.setFixedSize(40,40)

       bar.addStretch()
       bar.addWidget(alert_label)
       bar.addWidget(onoff_label)
       bar.setStretch(0,6)
       bar.setStretch(1,1)
       bar.setStretch(2,1)
       
       layout.addLayout(bar)
       layout.addWidget(label)
       
       layout.setStretch(0,1)
       layout.setStretch(1,3)
       obj.setLayout(layout)
       
       img = QLabel(obj)
       img.setPixmap(self.att_img[text])
       img.setFixedSize(QSize(80,80))
       img.setContentsMargins(5,5,5,5)
       img.setScaledContents(True)
       pos = QPoint(0,0)
       img.move(pos)
    
    '''
      Costruisce il frame di un lotto
    '''
    def build_frame_lotto(self,obj, name, text):
       
       obj.setObjectName(name)
       obj.setScaledContents(True)

       layout = QVBoxLayout()

       label = QLabel("")
       label.setObjectName("nome_lotto")
       label.setAlignment(Qt.AlignCenter)
       alert_bar = QHBoxLayout()
       
       alert_frame_lotto = QLabel("")
       alert_frame_lotto.setObjectName("alert_frame_lotto")
       alert_frame_lotto.setScaledContents(True)
       alert_frame_lotto.setFixedSize(40,40)

       alert_bar.addWidget(alert_frame_lotto)
       alert_bar.addStretch()
       alert_bar.setStretch(0,1)
       alert_bar.setStretch(1,5)
       
       layout.addLayout(alert_bar)
       layout.addWidget(label)
       
       layout.setStretch(0,1)
       layout.setStretch(1,6)
       obj.setLayout(layout)
    
    '''
      Crea la gui
    '''

    def setup_ui(self,ui):
       
       self.att_img = {}
       
       self.att_img["Pompa idrica"] = QPixmap("img/pump.png").scaled(200,200,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
       self.att_img["De/Umidificatore"] = QPixmap("img/umid.png").scaled(200,200,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
       self.att_img["Impianto riscaldamento/raffrescamento"] = QPixmap("img/cooler.png").scaled(200,200,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
       self.att_img["Serbatoio CO2"] = QPixmap("img/serb.png").scaled(200,200,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

       self.alert_frame_lotto = {}
       self.main_container = QHBoxLayout()
       self.frame_settore = QFrame()
       self.frame_settore.setObjectName("big_frame_settore")
       
       vlayout = QVBoxLayout()

       hlayout0 = QHBoxLayout()
       hlayout0.addStretch()
       self.data_label = QLabel("qui data")
       self.data_label.setObjectName("data_label")
       hlayout0.addWidget(self.data_label)
       hlayout0.setStretch(0,15)
       hlayout0.setStretch(1,1)

       hlayout1 = QHBoxLayout()
       hlayout1.setSpacing(10)

       self.frame_umid = QFrame()
       self.build_frame_att(self.frame_umid,"frame_umid","De/Umidificatore")
       self.alert_umid = self.frame_umid.findChildren(QLabel, "alert_label")[0]
       self.onoff_umid = self.frame_umid.findChildren(QLabel, "onoff_label")[0]
       
       self.frame_temp_reg = QFrame()
       self.build_frame_att(self.frame_temp_reg,"frame_temp_reg","Impianto riscaldamento/raffrescamento")
       self.alert_temp_reg = self.frame_temp_reg.findChildren(QLabel, "alert_label")[0]
       self.onoff_temp_reg = self.frame_temp_reg.findChildren(QLabel, "onoff_label")[0]

       self.frame_co2 = QFrame()
       self.build_frame_att(self.frame_co2,"frame_co2","Serbatoio CO2")
       self.alert_co2 = self.frame_co2.findChildren(QLabel, "alert_label")[0]
       self.onoff_co2 = self.frame_co2.findChildren(QLabel, "onoff_label")[0]

       hlayout1.addWidget(self.frame_umid)
       hlayout1.addWidget(self.frame_temp_reg)
       hlayout1.addWidget(self.frame_co2)

       hlayout2 = QHBoxLayout()
       
       pompa_layout = QVBoxLayout()
       pompa_layout.addStretch()

       self.frame_pompa = QFrame()
       self.build_frame_att(self.frame_pompa,"frame_pompa","Pompa idrica")
       self.alert_pompa = self.frame_pompa.findChildren(QLabel, "alert_label")[0]
       self.onoff_pompa = self.frame_pompa.findChildren(QLabel, "onoff_label")[0]

       pompa_layout.addWidget(self.frame_pompa)
       pompa_layout.addStretch()
       
       pompa_layout.setStretch(0,1)
       pompa_layout.setStretch(1,1)
       pompa_layout.setStretch(2,1)

       self.frame_lotti = QFrame()
       self.frame_lotti.setObjectName("frame_lotti")
       
       self.lotti_layout = QGridLayout()
       rows, cols = 2, 4
       self.lotti = []
       
       for i in range(rows):
            for j in range(cols):
                frame = QLabel()
                self.build_frame_lotto(frame,"frame_lotto_sing","Lotto {}".format(i*cols+j + 1))
                self.lotti.append(frame)
                self.lotti_layout.addWidget(frame,i,j)
       
       self.frame_lotti.setLayout(self.lotti_layout)
       hlayout2.addLayout(pompa_layout)
       hlayout2.addWidget(self.frame_lotti)
       hlayout2.setStretch(0,1)
       hlayout2.setStretch(1,5)
       
       hlayout3 = QHBoxLayout()
       self.indietro = QPushButton("indietro")
       self.label_coltura = QLabel()
       self.button_raccogli = QPushButton("Raccogli tutto")
       self.vista_selezione_coltura = Vista_Selezione_Coltura(ui,ui.main_window)
       self.button_pianta = QPushButton("Pianta tutto")
       self.error_label = QLabel()
       self.error_label.setObjectName("error_label")
       
       hlayout3.addWidget(self.indietro)
       hlayout3.addStretch()
       hlayout3.addWidget(self.error_label)
       hlayout3.addStretch()
       hlayout3.addWidget(self.label_coltura)
       hlayout3.addWidget(self.button_raccogli)
       hlayout3.addWidget(self.vista_selezione_coltura)
       hlayout3.addWidget(self.button_pianta)
       hlayout3.setSpacing(10)

       stretch = [1, 1, 4, 1, 1, 1, 3, 1]

       for i, s in enumerate(stretch):
            hlayout3.setStretch(i,s)

       vlayout.addLayout(hlayout0)
       vlayout.addLayout(hlayout1)
       vlayout.addLayout(hlayout2)
       vlayout.addLayout(hlayout3)
       
       vlayout.setStretch(0,1)
       vlayout.setStretch(1,4)
       vlayout.setStretch(2,15)
       vlayout.setStretch(3,1)

       self.frame_settore.setLayout(vlayout)
       self.main_container.addWidget(self.frame_settore)
       ui.setLayout(self.main_container)