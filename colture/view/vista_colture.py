from colture.view.ui_colture import Ui_Colture
from colture.controller.contr_lista_colture import Contr_Lista_Colture
from util.simple_window  import Simple_Window
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt

'''
    Implementazione della classe Vista_Colture
    Implementa la vista del database colture
'''

class Vista_Colture(Simple_Window):

    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            colture.view.ui_colture.setup_ui(self,ui)
            colture.controller.contr_lista_colture.carica_colture(self)
            util.simple_window.start_time_refresher(self)
    '''
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
    
    '''
        Inserisce le colture nel QListWidget
    '''

    def ricarica(self):
        self.ui.lista.clear()
        for i in self.elementi_lista:
            self.ui.lista.addItem(QtWidgets.QListWidgetItem(i))
    '''
        Filtra la lista di colture in base alla stringa cercata
        Viene richiamata quando cambia il testo nella search bar
        Percorso della funzione richiamata:
            colture.controller.contr_lista_colture.serch(self,string)
    '''

    def on_search(self):
        self.elementi_lista = self.controller.search(self.ui.searchbar.text())
        self.ricarica()
    
    '''
        Resetta i campi informativi visualizzati nella scheda tecnica al variare
        della coltura selezionata
        Percorso della funzione richiamata:
            colture.controller.contr_lista_colture.get_id_by_name(self,string)
            colture.controller.contr_lista_colture.get_soluzione(self,id)
            colture.controller.contr_lista_colture.get_profilo_luce(self,id)
            colture.controller.contr_lista_colture.get_property(self,id,prop)
    '''

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
    
    '''
        Cambia l'immagine al variare della coltura selezionata
        Percorso delle funzioni chiamate:
            colture.controller.contr_lista_colture.get_id_by_name(self,string)
    '''

    def change_photo(self):
        selected = self.ui.lista.currentItem()
        if selected is not None:
            id_coltura = self.controller.get_id_by_name(selected.text())
            self.ui.fotopianta.setPixmap(self.photo_list[id_coltura])