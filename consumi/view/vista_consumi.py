from consumi.view.ui_consumi import Ui_Consumi
from consumi.controller.contr_consumi import Contr_Consumi
from PyQt5.QtWidgets import QWidget
from util.simple_window import Simple_Window


# Vista dei consumi: grafici del consumo elettrico e idrico per periodo.
class Vista_Consumi(Simple_Window):

   # Ridisegna il grafico dei consumi elettrici per il periodo selezionato.
   def on_change_elettro(self):
        data = self.controller.on_change_elettro(self.ui.combo_elettro.currentIndex(),self.time_thread.get_time())
        self.ui.grafico_elett.clear()
        self.ui.grafico_elett.plot(data[0],data[1])

   # Ridisegna il grafico dei consumi idrici per il periodo selezionato.
   def on_change_idro(self):
        data = self.controller.on_change_idro(self.ui.combo_idro.currentIndex(),self.time_thread.get_time())
        self.ui.grafico_acqua.clear()
        self.ui.grafico_acqua.plot(data[0],data[1])

   # Costruisce la UI e collega le combo box dei periodi.
   def __init__(self, parent_ui, main_window):
        super(Vista_Consumi,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Consumi()
        self.ui = Ui_Consumi()
        self.ui.setup_ui(self)
        self.start_time_refresher(self.ui.data_ora)
        self.ui.indietro.clicked.connect(self.go_back)
        self.ui.combo_elettro.activated.connect(self.on_change_elettro)
        self.ui.combo_idro.activated.connect(self.on_change_idro)
