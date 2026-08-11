from attuatore_generico.serbCO2.view.vista_serbCO2 import Vista_SerbCO2
from attuatore_generico.temp_reg.view.vista_temp_reg import Vista_Temp_Reg
from attuatore_generico.umid.view.vista_umid import Vista_Umid
from attuatore_generico.pompa.view.vista_pompa import Vista_Pompa
from lotto.view.vista_lotto import Vista_Lotto
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from avvisi.view.notifica import Notifica


# Notifica relativa a un attuatore fuori dai valori consigliati.
class Notifica_Att(Notifica):

    # Costruisce la notifica scegliendo icona, testo e vista in base al tipo di attuatore.
    def __init__(self, parent_ui, main_window, id, nome_att):

        nome_classe = {}
        abbr_ext = {}
        img = {}

        abbr_ext["pompa"] = "La pompa\n"
        nome_classe["pompa"] = Vista_Pompa
        img["pompa"] = QPixmap("img/pump.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)

        abbr_ext["umid"] = "Il de/umidificatore\n"
        nome_classe["umid"] = Vista_Umid
        img["umid"] = QPixmap("img/umid.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)

        abbr_ext["temp_reg"] = "L'impianto di \nraffrescamento/\nriscaldamento\n"
        nome_classe["temp_reg"] = Vista_Temp_Reg
        img["temp_reg"] = QPixmap("img/cooler.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)

        abbr_ext["serb_co2"] = "Il serbatoio di CO2\n"
        nome_classe["serb_co2"] = Vista_SerbCO2
        img["serb_co2"] = QPixmap("img/serb.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)

        abbr_ext["luce_reg"] = "L'impianto di\nilluminazione\n"
        nome_classe["luce_reg"] = Vista_Lotto
        img["luce_reg"] = QPixmap("img/lamp.png").scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)

        super().__init__(parent_ui,
                        main_window,
                        [id],
                        [nome_classe[nome_att]],
                        "{} n° {} non è impostato\n sui valori consigliati".format(abbr_ext[nome_att], id),
                        img[nome_att])

        self.ui.img.setStyleSheet("background-color: yellow")
        self.nome_att = nome_att

    # Restituisce il nome abbreviato dell'attuatore della notifica.
    def get_nome_att(self):
        return self.nome_att
