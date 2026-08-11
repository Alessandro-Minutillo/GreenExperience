from attuatore_generico.temp_reg.view.ui_temp_reg import Ui_Temp_Reg
from attuatore_generico.temp_reg.controller.contr_temp_reg import Contr_Temp_Reg
from util.simple_window import Simple_Window


# Vista del regolatore di temperatura: imposta la temperatura obiettivo e lo stato acceso/spento.
class Vista_Temp_Reg(Simple_Window):

    # Applica al model la temperatura impostata nella spinbox.
    def connect_temp(self):
        self.controller.change_temp(self.ui.spinBox.value())

    # Inverte lo stato acceso/spento del regolatore.
    def switch_onoff(self):
        self.controller.on_off()

    # Aggiorna a ogni refresh i consumi corrente e medio mostrati.
    def refresh_gui(self):
        self.ui.valore_corrente.setText(str(self.controller.get_consumo_real(self.ui.spinBox.value()))+" KWh")
        self.ui.valore_medio.setText(str(self.controller.get_consumo_medio(self.ui.spinBox.value()))+" KWh")

    # Costruisce la UI, imposta i valori iniziali e disabilita i comandi in modalità guest.
    def __init__(self, parent_ui, main_window, id):
        super(Vista_Temp_Reg,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Temp_Reg(id)
        self.ui = Ui_Temp_Reg()
        self.ui.setup_ui(self)
        self.start_gui_refresher()

        self.start_time_refresher(self.ui.data_ora)
        self.ui.indietro.clicked.connect(self.go_back)

        self.ui.onoff_att.setChecked(self.controller.get_switch())
        self.ui.spinBox.setValue(self.controller.get_temp_ob())
        self.ui.onoff_att.stateChanged.connect(self.switch_onoff)
        self.ui.spinBox.valueChanged.connect(self.connect_temp)
        self.ui.valore_consigliato.setText(str(self.controller.get_temp_cons())+" °C")
        self.ui.nome_coltura.setText(self.controller.get_coltura())

        if self.main_window.mode == "guest":
            self.ui.onoff_att.setEnabled(False)
            self.ui.spinBox.setEnabled(False)
