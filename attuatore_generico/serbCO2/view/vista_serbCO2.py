from attuatore_generico.serbCO2.view.ui_serbCO2 import Ui_SerbCO2
from attuatore_generico.serbCO2.controller.contr_serbCO2 import Contr_SerbCO2
from util.simple_window import Simple_Window


# Vista del serbatoio di CO2: imposta il livello obiettivo e lo stato acceso/spento.
class Vista_SerbCO2(Simple_Window):

    # Applica al model il livello di CO2 impostato nella spinbox.
    def connect_co2(self):
        self.controller.change_co2(self.ui.spinBox.value())

    # Inverte lo stato acceso/spento del serbatoio.
    def switch_onoff(self):
        self.controller.on_off()

    # Aggiorna a ogni refresh i consumi corrente e medio mostrati.
    def refresh_gui(self):
        self.ui.valore_corrente.setText(str(self.controller.get_consumo_real(self.ui.spinBox.value()))+" KWh")
        self.ui.valore_medio.setText(str(self.controller.get_consumo_medio(self.ui.spinBox.value()))+" KWh")

    # Costruisce la UI, imposta i valori iniziali e disabilita i comandi in modalità guest.
    def __init__(self, parent_ui, main_window, id):

        super(Vista_SerbCO2,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_SerbCO2(id)
        self.ui = Ui_SerbCO2()
        self.ui.setup_ui(self)
        self.start_gui_refresher()

        self.start_time_refresher(self.ui.data_ora)
        self.ui.indietro.clicked.connect(self.go_back)

        self.ui.onoff_att.setChecked(self.controller.get_switch())
        self.ui.spinBox.setValue(self.controller.get_co2_ob())
        self.ui.onoff_att.stateChanged.connect(self.switch_onoff)
        self.ui.spinBox.valueChanged.connect(self.connect_co2)
        self.ui.valore_consigliato.setText(str(self.controller.get_co2_cons())+" ppm")
        self.ui.nome_coltura.setText(self.controller.get_coltura())

        if self.main_window.mode == "guest":
            self.ui.onoff_att.setEnabled(False)
            self.ui.spinBox.setEnabled(False)
