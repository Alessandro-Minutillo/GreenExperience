from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from lotto.view.vista_lotto import Vista_Lotto
from avvisi.view.notifica import Notifica


# Notifica che segnala un lotto in cui è possibile piantare.
class Notifica_Pianta(Notifica):

    # Costruisce la notifica con collegamento alla vista del lotto.
    def __init__(self, parent_ui, main_window, id):
        super().__init__(parent_ui,
                        main_window,
                        [id],
                        [Vista_Lotto],
                        "Pianta il lotto {}".format(id),
                        QPixmap("img/planting.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation),
                        ["vai al lotto"])
