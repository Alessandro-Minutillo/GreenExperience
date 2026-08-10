from PyQt5 import QtWidgets,QtCore
from attuatore_generico.pompa.view.ui_pompa import Ui_Pompa
from util.simple_window import Simple_Window
from attuatore_generico.pompa.controller.contr_pompa import Contr_pompa

"""
    Implementazione della classe Vista_Pompa
    Contiene i widget necessari all' interazione con ' utente e le funzioni che le gestiscono.

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Vista_Pompa(Simple_Window):

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

    """
        Effettua il toggle dell' interruttore della pompa, ossia la accende se spenta e la spegne se accesa
        Percorso delle funzioni richiamate:
            attuatore_generico.pompa.controller.controller_pompa.on_off()
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def toggleswitch(self):
        self.controller.on_off()
    """
        Effettua il cambio del ph della soluzione in cui sono le piante del settore
        Percorso delle funzioni richiamate:
        attuatore_generico.pompa.controller.controller_pompa.on_change_ph(self.ui.doubleSpinBox_1_ph.cleanText().replace(',','.'))
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def on_change_ph(self):
        self.controller.on_change_ph(self.ui.doubleSpinBox_1_ph.cleanText().replace(',','.'))
        self.ui.valore1.setText(self.ui.doubleSpinBox_1_ph.cleanText())
    """
        Effettua il cambio della salinità della soluzione in cui sono le piante del settore
        Percorso delle funzioni richiamate:
        attuatore_generico.pompa.controller.controller_pompa.on_change_ec(self.ui.doubleSpinBox_2_ec.cleanText().replace(',','.'))
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def on_change_ec(self):
        self.controller.on_change_ec(self.ui.doubleSpinBox_2_ec.cleanText().replace(',','.'))
        self.ui.valore2.setText(self.ui.doubleSpinBox_2_ec.cleanText())
    """
        Effettua il cambio dei macroelementi della soluzione in cui sono le piante del settore
        Percorso delle funzioni richiamate:
            attuatore_generico.pompa.controller.controller_pompa.on_change_sol(self.ui.selectprofile.currentIndex()+1)
            self.refresh_table()
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def on_change_sol(self):
        self.controller.on_change_sol(self.ui.selectprofile.currentIndex()+1)
        self.refresh_table()

    """
        Disabilita la tabella dei macroelementi
        Percorso delle funzioni richiamate:
            Nessuna
        Parametri:
            Nessuno
        Return:
            Nessuno
    """

    def disable_table(self):
        for i in range(0,6):
            for j in range(0,2):
                self.ui.tabella.item(i,j).setFlags(QtCore.Qt.NoItemFlags)
                self.ui.tabella.item(i,j).setFlags(QtCore.Qt.ItemIsEnabled)
    
    """
        Effettua il refresh della tabella dei macroelementi quando vengono cambiate le impostazioni
        Percorso delle funzioni richiamate:
            self.controller.get_sol()
            self.controller.get_sol_cons()
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
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

    def refresh_gui(self):
        val_consumo_ele=self.controller.get_consumo_el()
        val_consumo_idro=self.controller.get_consumo_idro()
        self.ui.valore3.setText(str(val_consumo_ele))
        self.ui.valore4.setText(str(val_consumo_idro))
