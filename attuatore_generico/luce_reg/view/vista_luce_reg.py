from PyQt5.QtWidgets import QFrame
from attuatore_generico.luce_reg.controller.contr_luce_reg import Contr_Luce_Reg
from attuatore_generico.luce_reg.view.ui_luce_reg import Ui_Luce_Reg

'''
    Implentazione della classe Vista_Luce_Reg
    Implementa la vista dell'impianto di illuminazione
'''

class Vista_Luce_Reg(QFrame):
    
    '''
        Setta il tipo di luce impostato nell'impianto di illuminazione 
        Viene richiamata quando cambia l'indice della combo box
        del tipo di luce
        
        Percorso della funzione chiamata:
            attuatore_generico.luce_reg.controller.contr_luce_reg.change_luce(self,tipo)
    '''

    def change_luce(self):
        tipo = self.ui.combo_luce.currentText()
        self.controller.change_luce(tipo)

    '''
        Cambia lo stato acceso/spento dell'attuatore
        Viene richiamata quando cambia lo stato di Animated Toggle

        Percorso della funzione chiamata:
            attuatore_generico.interface.contr_att.on_off(self)
    '''

    def switch_onoff(self):
        self.controller.on_off()
    
    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            attuatore_generico.luce_reg.view.ui_luce_reg.setup_ui(self,ui)
    '''

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