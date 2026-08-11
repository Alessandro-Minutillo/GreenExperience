from attuatore_generico.interface.ui_att import Ui_Att
from PyQt5.QtWidgets import QWidget


# Vista base di un attuatore generico: costruisce la GUI tramite Ui_Att.
class Vista_Att(QWidget):

    # Memorizza vista parent e finestra principale, poi inizializza la UI.
    def __init__ (self, parent_ui, main_window):
        super(Vista_Att,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ui=Ui_Att()
        self.ui.setup_Ui(self)
