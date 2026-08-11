from produttività.view.ui_prod import Ui_Prod
from produttività.controller.contr_prod import Contr_Prod
from util.simple_window import Simple_Window


# Vista della produttività: grafico della resa per coltura e periodo.
class Vista_Prod(Simple_Window):

    # Ridisegna il grafico in base alla coltura e al periodo selezionati.
    def on_change_tipo_coltura(self):
        self.ui.grafico.clear()
        dati=self.controller.on_change_tipo_coltura(self.ui.tipo_coltura.get_current_index(),self.ui.periodo_interesse.currentIndex(),self.time_thread.get_time())
        self.ui.grafico.plot(dati[1],dati[0])

    # Costruisce la UI, traccia il grafico iniziale e collega le combo box.
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
