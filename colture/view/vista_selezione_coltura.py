from PyQt5.QtWidgets import QWidget
from colture.controller.contr_lista_colture import Contr_Lista_Colture
from colture.view.ui_selezione_coltura import Ui_Selezione_Coltura


# Vista di selezione coltura tramite combo box.
class Vista_Selezione_Coltura(QWidget):

    # Restituisce il nome della coltura selezionata.
    def get_current_coltura(self):
        return self.ui.combo_coltura.currentText()

    # Restituisce l'id della coltura selezionata.
    def get_current_coltura_id(self):
        return self.controller.get_id_by_name(self.ui.combo_coltura.currentText())

    # Restituisce l'indice selezionato nella combo box.
    def get_current_index(self):
        return self.ui.combo_coltura.currentIndex()

    # Costruisce la UI e popola la combo box con tutte le colture.
    def __init__(self,parent_ui,main_window):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Lista_Colture()
        self.ui = Ui_Selezione_Coltura()
        self.ui.setup_ui(self)

        for colt in self.controller.get_all().values():
            self.ui.combo_coltura.addItem(colt.get_name())
