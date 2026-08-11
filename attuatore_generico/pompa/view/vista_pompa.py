from PyQt5 import QtWidgets,QtCore
from attuatore_generico.pompa.view.ui_pompa import Ui_Pompa
from util.simple_window import Simple_Window
from attuatore_generico.pompa.controller.contr_pompa import Contr_pompa


# Vista della pompa: widget di controllo di pH, EC, soluzione e stato acceso/spento.
class Vista_Pompa(Simple_Window):

    # Costruisce la UI, collega il controller e disabilita i comandi in modalità guest.
    def __init__ (self, parent_ui, main_window, id):
        super(Vista_Pompa,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ui=Ui_Pompa()
        self.ui.setup_ui(self)

        self.start_time_refresher(self.ui.data_label)
        self.controller= Contr_pompa(id)
        self.ui.indietro.clicked.connect(self.go_back)
        self.setui()
        self.start_gui_refresher()

        if self.main_window.mode == 'guest':
            self.ui.doubleSpinBox_1_ph.setEnabled(False)
            self.ui.doubleSpinBox_2_ec.setEnabled(False)
            self.ui.onoff_pompa.setEnabled(False)
            self.ui.selectprofile.setEnabled(False)

    # Inverte lo stato acceso/spento della pompa.
    def toggleswitch(self):
        self.controller.on_off()

    # Applica il nuovo pH dalla spinbox e aggiorna la label.
    def on_change_ph(self):
        self.controller.on_change_ph(self.ui.doubleSpinBox_1_ph.cleanText().replace(',','.'))
        self.ui.valore1.setText(self.ui.doubleSpinBox_1_ph.cleanText())

    # Applica la nuova salinità (EC) dalla spinbox e aggiorna la label.
    def on_change_ec(self):
        self.controller.on_change_ec(self.ui.doubleSpinBox_2_ec.cleanText().replace(',','.'))
        self.ui.valore2.setText(self.ui.doubleSpinBox_2_ec.cleanText())

    # Applica il profilo soluzione selezionato e aggiorna la tabella.
    def on_change_sol(self):
        self.controller.on_change_sol(self.ui.selectprofile.currentIndex()+1)
        self.refresh_table()

    # Rende non modificabili le celle della tabella dei macroelementi.
    def disable_table(self):
        for i in range(0,6):
            for j in range(0,2):
                self.ui.tabella.item(i,j).setFlags(QtCore.Qt.NoItemFlags)
                self.ui.tabella.item(i,j).setFlags(QtCore.Qt.ItemIsEnabled)

    # Ricarica la tabella con i macroelementi della soluzione attuale e di quella consigliata.
    def refresh_table(self):
        soluzione=self.controller.get_sol()
        self.ui.tabella.setItem(0,0,QtWidgets.QTableWidgetItem(str(soluzione.get_property("quant_N"))))
        self.ui.tabella.setItem(1,0,QtWidgets.QTableWidgetItem(str(soluzione.get_property("quant_K"))))
        self.ui.tabella.setItem(2,0,QtWidgets.QTableWidgetItem(str(soluzione.get_property("quant_P"))))
        self.ui.tabella.setItem(3,0,QtWidgets.QTableWidgetItem(str(soluzione.get_property("quant_Mg"))))
        self.ui.tabella.setItem(4,0,QtWidgets.QTableWidgetItem(str(soluzione.get_property("quant_Fe"))))
        self.ui.tabella.setItem(5,0,QtWidgets.QTableWidgetItem(str(soluzione.get_property("quant_Ca"))))

        sol_cons=self.controller.get_sol_cons()
        self.ui.tabella.setItem(0,1,QtWidgets.QTableWidgetItem(str(sol_cons.get_property("quant_N"))))
        self.ui.tabella.setItem(1,1,QtWidgets.QTableWidgetItem(str(sol_cons.get_property("quant_K"))))
        self.ui.tabella.setItem(2,1,QtWidgets.QTableWidgetItem(str(sol_cons.get_property("quant_P"))))
        self.ui.tabella.setItem(3,1,QtWidgets.QTableWidgetItem(str(sol_cons.get_property("quant_Mg"))))
        self.ui.tabella.setItem(4,1,QtWidgets.QTableWidgetItem(str(sol_cons.get_property("quant_Fe"))))
        self.ui.tabella.setItem(5,1,QtWidgets.QTableWidgetItem(str(sol_cons.get_property("quant_Ca"))))
        self.disable_table()

    # Popola i widget con i valori iniziali e collega i segnali di modifica.
    def setui(self):
        self.refresh_table()
        self.ui.selectprofile.addItems(self.controller.get_list_profiles())
        self.ui.onoff_pompa.setChecked(self.controller.get_switch())
        self.ui.onoff_pompa.stateChanged.connect(self.toggleswitch)
        self.ui.doubleSpinBox_1_ph.valueChanged.connect(self.on_change_ph)
        self.ui.doubleSpinBox_2_ec.valueChanged.connect(self.on_change_ec)
        self.ui.selectprofile.activated.connect(self.on_change_sol)
        val_ph=self.controller.get_ph()
        val_ec=self.controller.get_ec()
        cons_ph=self.controller.get_ph_cons()
        cons_ec=self.controller.get_ec_cons()
        self.ui.scritta2.setText(str(cons_ec))
        self.ui.scritta1.setText(str(cons_ph))
        self.ui.doubleSpinBox_1_ph.setValue(val_ph)
        self.ui.doubleSpinBox_2_ec.setValue(val_ec)
        self.ui.valore1.setText(str(val_ph))
        self.ui.valore2.setText(str(val_ec))

    # Aggiorna a ogni refresh i consumi elettrico e idrico mostrati.
    def refresh_gui(self):
        val_consumo_ele=self.controller.get_consumo_el()
        val_consumo_idro=self.controller.get_consumo_idro()
        self.ui.valore3.setText(str(val_consumo_ele))
        self.ui.valore4.setText(str(val_consumo_idro))
