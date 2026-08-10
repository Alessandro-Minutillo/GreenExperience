from PyQt5.QtWidgets import QAbstractItemView, QListWidget, QVBoxLayout, QGroupBox

'''
    Implementazione della classe Ui_Bacheca
    Implementa la gui del widget che rappresenta una bacheca
    nella vista avvisi
'''

class Ui_Bacheca():
    
    '''
        Costruisce la gui
        Parametri:
            (avvisi.view.vista_bacheca) ui, vista bacheca
    '''

    def setup_ui(self,ui):
     self.main_container = QVBoxLayout()
     gbox = QGroupBox(ui.title)
     gbox.setObjectName("gbox")
     layout = QVBoxLayout()
     self.list_notify = QListWidget()
     self.list_notify.setSelectionMode(QAbstractItemView.NoSelection)
     layout.addWidget(self.list_notify)
     gbox.setLayout(layout)
     self.main_container.addWidget(gbox)
     ui.setLayout(self.main_container)