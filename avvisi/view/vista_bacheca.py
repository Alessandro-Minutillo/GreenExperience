from avvisi.view.notifica_vuota import Notifica_Vuota
from util.gui_refresher import Gui_Refresher
from avvisi.view.ui_bacheca import Ui_Bacheca
from PyQt5.QtWidgets import QListWidgetItem, QWidget

'''
    Implementazione della classe Vista_Bacheca
    Definisce un'interfaccia per la vista di una bacheca
'''

class Vista_Bacheca(QWidget):
    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            avvisi.view.ui_bacheca.setup_ui(self,ui)
    '''

    def __init__(self, parent_ui, main_window, title):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.title = title
        self.ui = Ui_Bacheca()
        self.ui.setup_ui(self)

    '''
        Istanzia un thread che esegue il refresh della gui
    '''

    def start_gui_refresher(self):
            self.thread = Gui_Refresher(100)
            self.thread.refresh_signal.connect(self.refresh_gui)
            self.thread.start()
    
    '''
        Aggiunge alla visualizzazione una notifica vuota quando
        non ci sono messaggi di interesse per l'utente
    '''

    def fill_empty_list(self):
        if not self.ui.list_notify.count():
            self.add_widget(Notifica_Vuota(self, self.main_window))

    '''
        Metodo ausiliario che inserisce un widget all'interno
        di un QListWidget
        Parametri:
            (QWidget) widget
    '''

    def add_widget(self, widget):
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.ui.list_notify.addItem(item)
        self.ui.list_notify.setItemWidget(item,widget)