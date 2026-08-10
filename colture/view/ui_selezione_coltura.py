from PyQt5.QtWidgets import QComboBox, QVBoxLayout

'''
    Implementazione della classe Ui_Selezione_Coltura
    Crea la gui della vista selezione coltura
'''

class Ui_Selezione_Coltura():
    
    '''
        Crea la gui
    '''

    def setup_ui(self,ui):
       ui.setObjectName("widget_selezione_coltura")
       layout = QVBoxLayout()
       self.combo_coltura = QComboBox()
       layout.addWidget(self.combo_coltura)
       ui.setLayout(layout)