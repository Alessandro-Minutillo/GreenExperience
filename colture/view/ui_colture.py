from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

'''
    Implementazione della classe Ui_Colture
    Crea la gui della vista colture
'''

class Ui_Colture():

    '''
        Crea la gui
    '''

    def setup_ui(self, widget):

        #layout verticale più esterno
        self.layouttotale = QtWidgets.QVBoxLayout()
        
        #layout data
        self.layoutdata = QtWidgets.QHBoxLayout()
        self.data_ora = QtWidgets.QLabel(widget)
        self.data_ora.setObjectName("data_label")
        
        self.data_ora.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layoutdata.addWidget(self.data_ora)
        
         
        #layout principale
        
        self.layoutprincipale = QtWidgets.QHBoxLayout()
        
        self.layoutdestra = QtWidgets.QVBoxLayout()
        
        self.layoutsinistra =QtWidgets.QVBoxLayout()

        self.layoutinfopianta = QtWidgets.QHBoxLayout()

        #costruisco il layout di destra

        self.fotopianta = QtWidgets.QLabel("Seleziona una coltura per vedere le info")
        self.fotopianta.setScaledContents(True)
        self.fotopianta.setFixedSize(400,400)
        
        #creo il layoutstats per contenere le statistiche della pianta

        self.layoutstats = QtWidgets.QGridLayout()
        self.layoutstats.setContentsMargins(5,20,5,5)

        self.dati_pianta= {
        "nome_comune" : QtWidgets.QLabel(""),
        "nome_scientifico" : QtWidgets.QLabel(""),
        "descrizione" : QtWidgets.QLabel(""),
        "durata" : QtWidgets.QLabel(""),
        "prod_lotto" : QtWidgets.QLabel(""),
        "temp_cons" : QtWidgets.QLabel(""),
        "umid_cons" : QtWidgets.QLabel(""),
        "liv_co2_cons" : QtWidgets.QLabel(""),
        "pH_cons" : QtWidgets.QLabel(""),
        "ec_cons" : QtWidgets.QLabel(""),
        "id_soluzione_circolante" : QtWidgets.QLabel(""),
        "id_profilo_luce" : QtWidgets.QLabel("")
        }

        abbr_to_ext = {
        "nome_comune" : "Nome Comune",
        "nome_scientifico" : "Nome Scientifico",
        "descrizione" : "Descrizione",
        "durata" : "Durata (gg)",
        "prod_lotto" : "Resa per 10 mq",
        "temp_cons" : "Temperatura\nconsigliata (°C)",
        "umid_cons" : "Umidità\nconsigliata (%)",
        "liv_co2_cons" : "Livello di CO2\nconsigliato\n(ppm)",
        "pH_cons" : "Livello di pH\nconsigliato",
        "ec_cons" : "Livello di EC\nconsigliato",
        "id_soluzione_circolante" : "Soluzione\nCircolante",
        "id_profilo_luce" : "Profilo Luce"
        }

        self.status_widget = QtWidgets.QGroupBox()
        self.status_widget.setTitle("Scheda tecnica")
        self.status_widget.setAlignment(QtCore.Qt.AlignHCenter)
        self.status_widget.setLayout(self.layoutstats)
        self.status_widget.setObjectName("stats")
        
        self.layoutinfopianta.addWidget(self.fotopianta)
        self.layoutinfopianta.addWidget(self.status_widget)

        self.layoutinfopianta.setStretch(0,1)
        self.layoutinfopianta.setStretch(1,2)
        
        for i, prop in enumerate(self.dati_pianta.keys()):
            string = abbr_to_ext[prop]
            label = QtWidgets.QLabel(string)
            label.setObjectName("caratteristica")
            self.dati_pianta[prop].setWordWrap(True)
            self.layoutstats.addWidget(label, i, 0)
            
            if prop == "descrizione":
                scrollArea = QtWidgets.QScrollArea()
                scrollArea.setObjectName("scrollArea")
                scrollArea.setWidgetResizable(True)
                scrollArea.setFixedSize(250,75)
                scrollArea.setWidget(self.dati_pianta[prop])
                self.dati_pianta[prop].setObjectName("descrizione")
                self.layoutstats.addWidget(scrollArea, i, 1)
            else:
                self.layoutstats.addWidget(self.dati_pianta[prop], i, 1)
        
        #self.description = QtWidgets.QTextBrowser()
        
        self.layoutdestra.addLayout(self.layoutinfopianta)
        #self.layoutdestra.addWidget(self.description)

        self.layoutdestra.setStretch(0,4)
        self.layoutdestra.setStretch(1,1)

        #costruisco il layout di sinistra

        self.database= QtWidgets.QLabel()
        self.database.setObjectName("database_label")
        self.database.setText("Database colture")
        self.layoutsearch= QtWidgets.QHBoxLayout()
        self.searchbar =QtWidgets.QLineEdit()
        self.lista = QtWidgets.QListWidget()

        search_label = QtWidgets.QLabel()
        search_img = QPixmap("img/search.png").scaled(400,400,
                                                            QtCore.Qt.KeepAspectRatio,
                                                            QtCore.Qt.SmoothTransformation)
        search_label.setFixedSize(33,33)
        search_label.setPixmap(search_img)
        search_label.setScaledContents(True)

        self.layoutsearch.addWidget(search_label)
        self.layoutsearch.addWidget(self.searchbar)
        self.layoutsearch.setStretch(0,1)
        self.layoutsearch.setStretch(1,6)

        self.layoutsinistra.addWidget(self.database)
        self.layoutsinistra.addLayout(self.layoutsearch)
        self.layoutsinistra.addWidget(self.lista)

        self.layoutprincipale.addLayout(self.layoutsinistra)
        self.layoutprincipale.addLayout(self.layoutdestra)
        self.layoutprincipale.setStretch(0,1)
        self.layoutprincipale.setStretch(1,10)
        

        #layout tasto indietro

        self.layoutindietro = QtWidgets.QHBoxLayout()
        self.indietro = QtWidgets.QPushButton()

        self.layoutindietro.addWidget(self.indietro)
        self.layoutindietro.addStretch()

        self.layoutindietro.setStretch(0, 1)
        self.layoutindietro.setStretch(1, 6)
        
        #inserisco tutto nel layout più esterno        
        self.layouttotale.addLayout(self.layoutdata)
        self.layouttotale.addLayout(self.layoutprincipale)
        self.layouttotale.addLayout(self.layoutindietro)
        
        self.layouttotale.setStretch(0, 2)
        self.layouttotale.setStretch(1, 24)
        self.layouttotale.setStretch(2, 3)

        widget.setLayout(self.layouttotale)
        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    '''
        Setta testi nei widget
    '''

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("layout_base", "GreenExperience"))
        self.data_ora.setText(_translate("widget", "DATA/ORA"))
        self.indietro.setText(_translate("widget", "indietro"))