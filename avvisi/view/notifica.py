from avvisi.view.ui_notifica import Ui_Notifica
from PyQt5.QtWidgets import QWidget
from functools import partial


# Widget base di una notifica: icona, messaggio e pulsanti che aprono le viste collegate.
class Notifica(QWidget):

    # Costruisce la notifica e collega ogni pulsante alla vista e all'id corrispondenti.
    def __init__(self, parent_ui, main_window, ids, window_classes, message, icon, button_messages = ["intervieni"]):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ids = ids
        self.window_classes = window_classes
        self.message = message
        self.icon = icon
        self.button_messages = button_messages
        self.ui = Ui_Notifica()
        self.ui.setup_ui(self)

        for btn, wc, id in zip(self.ui.buttons, self.window_classes, self.ids):
            btn.clicked.connect(partial(self.on_click, wc, id))

    # Apre la vista della classe indicata per l'id indicato.
    def on_click(self, w_class, id):
        vista = w_class(self,self.main_window, id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    # Restituisce il primo id associato alla notifica.
    def get_id(self):
        if self.ids:
            return self.ids[0]
