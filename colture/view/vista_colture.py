from colture.view.ui_colture import Ui_Colture
from colture.controller.contr_lista_colture import Contr_Lista_Colture
from util.simple_window  import Simple_Window
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt


# Vista del catalogo colture: lista con ricerca, scheda tecnica e immagine.
class Vista_Colture(Simple_Window):

    # Costruisce la UI, carica le colture e precarica le immagini.
    def __init__(self,parent_ui,main_window):

        super(Vista_Colture,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Lista_Colture()
        self.ui = Ui_Colture()
        self.ui.setup_ui(self)

        self.elementi_lista = self.controller.carica_colture()
        self.photo_list = {}

        self.start_time_refresher(self.ui.data_ora)
        self.ricarica()
        self.ui.searchbar.textChanged.connect(self.on_search)

        for i in self.elementi_lista:
            self.photo_list[self.controller.get_id_by_name(i)] = QtGui.QPixmap("img/colture/"+str(self.controller.get_id_by_name(i))+".png").scaled(
                                                            400,
                                                            400,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.ui.indietro.clicked.connect(self.go_back)
        self.ui.lista.currentItemChanged.connect(self.update_pianta)
        self.ui.lista.currentItemChanged.connect(self.change_photo)

    # Ripopola il QListWidget con le colture attualmente filtrate.
    def ricarica(self):
        self.ui.lista.clear()
        for i in self.elementi_lista:
            self.ui.lista.addItem(QtWidgets.QListWidgetItem(i))

    # Filtra le colture in base al testo della search bar e ricarica la lista.
    def on_search(self):
        self.elementi_lista = self.controller.search(self.ui.searchbar.text())
        self.ricarica()

    # Aggiorna la scheda tecnica con i dati della coltura selezionata.
    def update_pianta(self):
        selected = self.ui.lista.currentItem()
        if selected is not None:
            id_coltura = self.controller.get_id_by_name(selected.text())

            for prop in self.ui.dati_pianta.keys():

                if prop == "id_soluzione_circolante":
                    self.ui.dati_pianta[prop].setText(self.controller.get_soluzione(id_coltura))

                elif prop == "id_profilo_luce":
                    self.ui.dati_pianta[prop].setText(self.controller.get_profilo_luce(id_coltura))

                else:
                    self.ui.dati_pianta[prop].setText(self.controller.get_property(id_coltura,prop))

    # Aggiorna l'immagine mostrata in base alla coltura selezionata.
    def change_photo(self):
        selected = self.ui.lista.currentItem()
        if selected is not None:
            id_coltura = self.controller.get_id_by_name(selected.text())
            self.ui.fotopianta.setPixmap(self.photo_list[id_coltura])
