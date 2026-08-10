from util.gui_refresher import Gui_Refresher
from centralina.view.ui_centralina import Ui_Centralina
from centralina.controller.contr_centralina import Contr_Centralina
from PyQt5.QtWidgets import QFrame

'''
    Implementazione della classe Vista_Centralina
    Implementa la vista di una centralina
'''

class Vista_Centralina(QFrame):
    
    '''
        Istanzia un thread che esegue il refresh della gui
    '''

    def start_gui_refresher(self):
        self.thread = Gui_Refresher()
        self.thread.refresh_signal.connect(self.refresh_gui)
        self.thread.start()

    '''
        Esegue il refresh della gui
        E' connessa al segnale emesso dal QThread Gui_Refresher
        istanziato da util.simple_window.start_gui_refresher(self)

        Percorso delle funzioni chiamate:
            centralina.controller.contr_centralina.get_temp(self)
            centralina.controller.contr_centralina.get_umid(self)
            centralina.controller.contr_centralina.get_liv_co2(self)
    '''

    def refresh_gui(self):
        self.ui.temp_label.setText(self.controller.get_temp())
        self.ui.umid_label.setText(self.controller.get_umid())
        self.ui.co2_label.setText(self.controller.get_liv_co2())

    '''
        Costruttore
        Parametri:
            (int) id, id della centralina
        Percorso della funzione chiamata:
            centralina.view.ui_centralina.setup_ui(self,ui)
    '''

    def __init__(self,id):
        super(Vista_Centralina,self).__init__()
        self.controller = Contr_Centralina(id)
        self.ui = Ui_Centralina()
        self.ui.setup_ui(self)
        self.start_gui_refresher()