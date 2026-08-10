from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from lotto.view.vista_lotto import Vista_Lotto
from avvisi.view.notifica import Notifica

'''
    Implementazione della classe Notifica_Raccolta
    Implementa un widget che rappresenta una notifica relativa
    ai lotti che è necessario raccogliere
'''

class Notifica_Raccolta(Notifica):

    '''
        Costruttore
        Parametri:
            (QWidget) parent_ui, vista parent;
            (QStackedWidget) main_window, stacked widget;
            (int) id, id del lotto
    '''

    def __init__(self, parent_ui, main_window, id):
        super().__init__(parent_ui, 
                        main_window, 
                        [id], 
                        [Vista_Lotto], 
                        "Raccogli il lotto {}".format(id),
                        QPixmap("img/time_out.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation),
                        ["vai al lotto"])
        
        self.ui.img.setStyleSheet("background-color: yellow")