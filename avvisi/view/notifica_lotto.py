from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from lotto.view.vista_lotto import Vista_Lotto
from avvisi.view.notifica import Notifica
from settore.view.vista_settore import Vista_Settore

'''
    Implementazione della class Notifica_Lotto
    Implementa un widget che rappresenta una notifica relativa
    allo stato di salute di un lotto
'''

class Notifica_Lotto(Notifica):

    '''
        Costruttore
        Parametri:
            (QWidget) parent_ui, vista parent;
            (QStackedWidget) main_window, stacked widget;
            (int) id, id del lotto;
            (int) id_settore, id del settore;
            (flaot) salute, indicatore di salute del lotto
    '''

    def __init__(self, parent_ui, main_window, id, id_settore, salute):
        self.id_settore = id_settore
        self.message = "La salute del lotto {} \nè al {} %.\nControlla e ripristina\ni parametri ambientali"
        self.salute = salute
        super().__init__(parent_ui, 
                        main_window, 
                        [id, id_settore], 
                        [Vista_Lotto, Vista_Settore], 
                        self.message.format(id, "{:.0f}".format(salute)),
                        QPixmap("img/ill.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation),
                        ["vai al lotto", "vai al settore"])
        
        self.ui.img.setStyleSheet("background-color: yellow")
    
    '''
        Ritorna l'indicatore numerico di salute del lotto cui la notifica fa riferimento
        Return:
            (int) indicatore di salute
    '''

    def get_salute(self):
        return self.salute