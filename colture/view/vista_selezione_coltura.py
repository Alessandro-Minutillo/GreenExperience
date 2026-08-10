from PyQt5.QtWidgets import QWidget
from colture.controller.contr_lista_colture import Contr_Lista_Colture
from colture.view.ui_selezione_coltura import Ui_Selezione_Coltura

'''
    Implementazione della classe Vista_Selezione_Coltura
    Implementa la vista che consente di scegliere una coltura
    mediante una combo box
'''

class Vista_Selezione_Coltura(QWidget):

    '''
        Restituisce la coltura attualmente selezionata
        Return:
            (string) nome coltura
    '''

    def get_current_coltura(self):
        return self.ui.combo_coltura.currentText()

    '''
        Restituisce l'id della coltura attualmente selezionata
        Return:
            (int) id, id della coltura
    '''

    def get_current_coltura_id(self):
        return self.controller.get_id_by_name(self.ui.combo_coltura.currentText())
    '''
        Restituisce l'indice attualmente selezionato della combo box
        Return:
            (int) indice
    '''

    def get_current_index(self):
        return self.ui.combo_coltura.currentIndex()
    
    '''
        Costruttore
        Percorso della funzione chiamata:
            colture.view.ui_selezione_coltura.setup_ui(self,ui)
    '''

    def __init__(self,parent_ui,main_window):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Lista_Colture()
        self.ui = Ui_Selezione_Coltura()
        self.ui.setup_ui(self)

        for colt in self.controller.get_all().values():
            self.ui.combo_coltura.addItem(colt.get_name())