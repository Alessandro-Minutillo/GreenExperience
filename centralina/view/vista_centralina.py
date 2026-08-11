from util.gui_refresher import Gui_Refresher
from centralina.view.ui_centralina import Ui_Centralina
from centralina.controller.contr_centralina import Contr_Centralina
from PyQt5.QtWidgets import QFrame


# Vista della centralina: mostra i valori rilevati di temperatura, umidità e CO2.
class Vista_Centralina(QFrame):

    # Avvia il thread di refresh della GUI.
    def start_gui_refresher(self):
        self.thread = Gui_Refresher()
        self.thread.refresh_signal.connect(self.refresh_gui)
        self.thread.start()

    # Aggiorna le label con i valori correnti rilevati dalla centralina.
    def refresh_gui(self):
        self.ui.temp_label.setText(self.controller.get_temp())
        self.ui.umid_label.setText(self.controller.get_umid())
        self.ui.co2_label.setText(self.controller.get_liv_co2())

    # Costruisce la UI e avvia il refresh.
    def __init__(self,id):
        super(Vista_Centralina,self).__init__()
        self.controller = Contr_Centralina(id)
        self.ui = Ui_Centralina()
        self.ui.setup_ui(self)
        self.start_gui_refresher()
