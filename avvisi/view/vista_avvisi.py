from avvisi.view.ui_avvisi import Ui_Avvisi
from util.simple_window import Simple_Window

'''
    Implementazione della classe Vista_Avvisi
    Implementa la vista in cui sono mostrate le bacheche
    contenenti notifiche 
'''

class Vista_Avvisi(Simple_Window):
    
    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            avvisi.view.ui_avvisi.setup_ui(self,ui)
            util.simple_window.start_time_refresher(self,data_label)
            util.simple_window.add_thread(self,thread)
    '''

    def __init__(self,parent_ui,main_window):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ui = Ui_Avvisi()
        self.ui.setup_ui(self)
        
        self.start_time_refresher(self.ui.data_label)
        self.add_thread(self.ui.bacheca1.thread)
        self.add_thread(self.ui.bacheca2.thread)
        self.add_thread(self.ui.bacheca3.thread)
        self.ui.indietro.clicked.connect(self.go_back)