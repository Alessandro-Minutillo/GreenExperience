from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from avvisi.view.notifica import Notifica

'''
    Implementazione della classe Notifica_Vuota
    Implementa un widget che rappresenta una notifica
    visualizzata quando non ci sono messaggi di interesse
    per l'utente
'''

class Notifica_Vuota(Notifica):
    
    '''
        Costruttore
        Parametri:
            (QWidget) parent_ui, vista parent;
            (QStackedWidget) main_window, stacked widget
    '''

    def __init__(self, parent_ui, main_window):
        super().__init__(parent_ui, 
                        main_window, 
                        [], 
                        [], 
                        "Nessuna notifica\nda mostrare",
                        QPixmap("img/ok.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation),
                        [])