from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from avvisi.view.notifica import Notifica


# Notifica mostrata quando non ci sono avvisi da segnalare.
class Notifica_Vuota(Notifica):

    # Costruisce la notifica vuota, senza pulsanti.
    def __init__(self, parent_ui, main_window):
        super().__init__(parent_ui,
                        main_window,
                        [],
                        [],
                        "Nessuna notifica\nda mostrare",
                        QPixmap("img/ok.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation),
                        [])
