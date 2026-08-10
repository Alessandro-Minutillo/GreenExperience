from avvisi.view.ui_notifica import Ui_Notifica
from PyQt5.QtWidgets import QWidget
from functools import partial

'''
    Implementazione dell'interfaccia notifica
    Definisce un'interfaccia per i widget che rappresentano una notifica
    Ogni notifica è caratterizzata da un'icona, da un messaggio e
    da un numero variabile di bottoni che, se cliccati, conducono ad
    altrettante viste
'''

class Notifica(QWidget):

    '''
        Costruttore
        Parametri:
            (QWidget) parent_ui, vista parent;
            (QStackedWidget) main_window, stacked widget;
            (list) ids, lista di id che identificano le viste da istanziare;
            (list) window_classes, lista delle classi delle viste da istanziare al click dei bottoni;
            (QPixmap) icon, file immagine dell'icona;
            (list) button_messages, lista dei testi da visualizzare all'interno dei bottoni 
    '''

    def __init__(self, parent_ui, main_window, ids, window_classes, message, icon, button_messages = ["intervieni"]):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ids = ids
        self.window_classes = window_classes
        self.message = message
        self.icon = icon
        self.button_messages = button_messages
        self.ui = Ui_Notifica()
        self.ui.setup_ui(self)
        
        for btn, wc, id in zip(self.ui.buttons, self.window_classes, self.ids):
            btn.clicked.connect(partial(self.on_click, wc, id))
    
    '''
        Istanzia una vista del tipo specificato, identificata dall'id specificato
        Viene richiamato al click di un bottone
        Parametri:
            (class) w_class, classe della vista;
            (int) id, id che identifica la vista
    '''

    def on_click(self, w_class, id):
        vista = w_class(self,self.main_window, id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)
    
    '''
        Ritorna il primo id della lista di id
        Return:
            (int) id
    '''

    def get_id(self):
        if self.ids:
            return self.ids[0]