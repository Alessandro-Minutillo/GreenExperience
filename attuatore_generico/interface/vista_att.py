from attuatore_generico.interface.ui_att import Ui_Att 
from PyQt5.QtWidgets import QWidget

'''
    Implementazione della class Vista_Att
    Definisce un'interfaccia per la vista di un generico attuatore
'''

class Vista_Att(QWidget):

    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            attuatore_generico.interface.ui_att.setup_Ui(self,ui)
    '''

    def __init__ (self, parent_ui, main_window):
        super(Vista_Att,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ui=Ui_Att()
        self.ui.setup_Ui(self)