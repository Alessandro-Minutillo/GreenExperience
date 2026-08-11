from attuatore_generico.umid.view.ui_umid import Ui_Umid
from attuatore_generico.umid.controller.contr_umid import Contr_Umid
from util.simple_window import Simple_Window


# Vista dell'umidificatore: imposta l'umidità obiettivo e lo stato acceso/spento.
class Vista_Umid(Simple_Window):

    # Applica al model l'umidità impostata nella spinbox.
    def connect_umid(self):
        self.controller.change_umid(self.ui.spinBox.value())

    # Inverte lo stato acceso/spento dell'umidificatore.
    def switch_onoff(self):
        self.controller.on_off()

    # Aggiorna a ogni refresh i consumi corrente e medio mostrati.
    def refresh_gui(self):
        self.ui.valore_corrente.setText(str(self.controller.get_consumo_real(self.ui.spinBox.value()))+" KWh")
        self.ui.valore_medio.setText(str(self.controller.get_consumo_medio(self.ui.spinBox.value()))+" KWh")

    # Costruisce la UI, imposta i valori iniziali e disabilita i comandi in modalità guest.
    def __init__(self, parent_ui, main_window, id):
        super(Vista_Umid,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Umid(id)
        self.ui = Ui_Umid()
        self.ui.setup_ui(self)
        self.start_gui_refresher()

        self.start_time_refresher(self.ui.data_ora)
        self.ui.indietro.clicked.connect(self.go_back)

        self.ui.onoff_att.setChecked(self.controller.get_switch())
        self.ui.spinBox.setValue(self.controller.get_umid_ob())
        self.ui.onoff_att.stateChanged.connect(self.switch_onoff)
        self.ui.spinBox.valueChanged.connect(self.connect_umid)
        self.ui.valore_consigliato.setText(str(self.controller.get_umid_cons())+" %")
        self.ui.nome_coltura.setText(self.controller.get_coltura())

        if self.main_window.mode == "guest":
            self.ui.onoff_att.setEnabled(False)
            self.ui.spinBox.setEnabled(False)
