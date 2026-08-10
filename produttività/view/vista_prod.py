from produttività.view.ui_prod import Ui_Prod
from produttività.controller.contr_prod import Contr_Prod
from util.simple_window import Simple_Window
"""
    Implementazione della classe Vista_Prod

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Vista_Prod(Simple_Window):
    """
        Viene chiamata quando l' utente seleziona l' impostazione per visualizzare il tipo di coltura o il periodo d'interesse
        Percorso delle funzioni richiamate:
            produttività.controller.contr_prod.on_change_tipo_coltura(self.ui.tipo_coltura.get_current_index(),self.ui.periodo_interesse.currentIndex(),self.time_thread.get_time())
        Parametri:
            Nessuno
        Return:
            Nessuno
    """    
    def on_change_tipo_coltura(self):
        self.ui.grafico.clear()
        dati=self.controller.on_change_tipo_coltura(self.ui.tipo_coltura.get_current_index(),self.ui.periodo_interesse.currentIndex(),self.time_thread.get_time())
        self.ui.grafico.plot(dati[1],dati[0])
    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            settore.view.ui_prod.setup_ui(self,ui)
            util.simple_window.start_time_refresher(self)
    '''
    def __init__(self, parent_ui, main_window):
        super(Vista_Prod,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Prod()
        self.ui = Ui_Prod()
        self.ui.setup_ui(self)
        self.start_time_refresher(self.ui.data_ora)
        dati=self.controller.on_change_tipo_coltura(self.ui.tipo_coltura.get_current_index(),self.ui.periodo_interesse.currentIndex(),self.time_thread.get_time())
        self.ui.grafico.plot(dati[1],dati[0])
        self.ui.indietro.clicked.connect(self.go_back)
        self.ui.periodo_interesse.activated.connect(self.on_change_tipo_coltura) 
        self.ui.tipo_coltura.ui.combo_coltura.activated.connect(self.on_change_tipo_coltura)