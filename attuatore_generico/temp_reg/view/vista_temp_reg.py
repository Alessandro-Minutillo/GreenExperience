from attuatore_generico.temp_reg.view.ui_temp_reg import Ui_Temp_Reg
from attuatore_generico.temp_reg.controller.contr_temp_reg import Contr_Temp_Reg
from util.simple_window import Simple_Window
"""
    Implementazione della classe Vista_Temp_Reg

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Vista_Temp_Reg(Simple_Window):

    """
        Funzione che permette di cambiare il valore dell'attributo info di Model_Temp_Reg relativo al campo "temp_ob" 
        Percorso della funzione richiamata:
            attuatore_generico.temp_reg.controller.change_temp(self.ui.spinBox.value())
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def connect_temp(self):
        self.controller.change_temp(self.ui.spinBox.value())

    """
        Funzione che cambia il valore booleano dell'interruttore dell'attuatore
        Percorso della funzione richiamata:
            attuatore_generico.interface.contr_att.on_off()
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def switch_onoff(self):
        self.controller.on_off()

    """
        Funzione che aggiorna i valori delle label valore_corrente e valore_medio
        Percorso delle funzioni richiamate:
            attuatore_generico.temp_reg.controller.get_consumo_real(self.ui.spinBox.value()))+" KWh")
            attuatore_generico.temp_reg.controller.get_consumo_medio(self.ui.spinBox.value()))+" KWh")
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def refresh_gui(self):
        self.ui.valore_corrente.setText(str(self.controller.get_consumo_real(self.ui.spinBox.value()))+" KWh")
        self.ui.valore_medio.setText(str(self.controller.get_consumo_medio(self.ui.spinBox.value()))+" KWh")

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