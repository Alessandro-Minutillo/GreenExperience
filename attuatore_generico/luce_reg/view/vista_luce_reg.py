from PyQt5.QtWidgets import QFrame
from attuatore_generico.luce_reg.controller.contr_luce_reg import Contr_Luce_Reg
from attuatore_generico.luce_reg.view.ui_luce_reg import Ui_Luce_Reg


# Vista dell'impianto di illuminazione: selezione tipo di luce e stato acceso/spento.
class Vista_Luce_Reg(QFrame):

    # Applica al model il tipo di luce scelto nella combo box.
    def change_luce(self):
        tipo = self.ui.combo_luce.currentText()
        self.controller.change_luce(tipo)

    # Inverte lo stato acceso/spento dell'impianto.
    def switch_onoff(self):
        self.controller.on_off()

    # Costruisce la UI, imposta i valori iniziali e disabilita i comandi in modalità guest.
    def __init__(self,parent_ui,main_window,id):
        super(Vista_Luce_Reg,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Luce_Reg(id)
        self.ui = Ui_Luce_Reg()
        self.ui.setup_ui(self)


        self.ui.onoff_luci.setChecked(self.controller.get_switch())
        self.ui.onoff_luci.stateChanged.connect(self.switch_onoff)

        index = self.ui.combo_luce.findText(self.controller.get_luce())
        self.ui.combo_luce.setCurrentIndex(index)
        self.ui.combo_luce.currentIndexChanged.connect(self.change_luce)

        if self.main_window.mode == "guest":
            self.ui.onoff_luci.setEnabled(False)
            self.ui.combo_luce.setEnabled(False)
