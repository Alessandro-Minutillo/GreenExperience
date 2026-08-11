from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from settore.view.ui_settore import Ui_Settore
from settore.controller.contr_settore import Contr_Settore
from PyQt5.QtWidgets import QLabel
from util.simple_window import Simple_Window
from lotto.view.vista_lotto import Vista_Lotto
from attuatore_generico.pompa.view.vista_pompa import Vista_Pompa
from attuatore_generico.temp_reg.view.vista_temp_reg import Vista_Temp_Reg
from attuatore_generico.umid.view.vista_umid import Vista_Umid
from attuatore_generico.serbCO2.view.vista_serbCO2 import Vista_SerbCO2
from functools import partial
from datetime import datetime
import locale


# Vista di un settore: griglia dei lotti, stato attuatori e azioni pianta/raccogli.
class Vista_Settore(Simple_Window):

    # Carica e ridimensiona le immagini di lotti, attuatori e icone di stato.
    def load_imgs(self):
        self.mywidth = 200
        self.myheight = 200

        self.full_lotto_img = QPixmap("img/area.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.empty_lotto_img = QPixmap("img/area2.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.img = {}

        self.img["ill"] = QPixmap("img/ill.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.img["on"] = QPixmap("img/on.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.img["off"] = QPixmap("img/off.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.img["vuoto"] = QPixmap("img/empty.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.img["coltivato"] = QPixmap("img/full.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.img["raccogliendo"] = QPixmap("img/picking.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.img["piantando"] = QPixmap("img/planting.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.img["time_out"] = QPixmap("img/time_out.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.img["alert"] = QPixmap("img/alert.png").scaled(self.mywidth,
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

    # Raccoglie tutti i lotti possibili del settore e mostra l'esito.
    def raccogli_tutto(self):
        num = self.controller.raccogli_tutto(self.time_thread.get_time())
        if num > 0:
            self.ui.error_label.setStyleSheet("color: #197d5a")
            self.ui.error_label.setText("raccogliendo {} lotti".format(num))
        else:
            self.ui.error_label.setStyleSheet("color: red")
            self.ui.error_label.setText("impossibile raccogliere lotti")

    # Pianta la coltura selezionata nei lotti disponibili e mostra l'esito.
    def pianta_tutto(self):
        selected_text = self.ui.vista_selezione_coltura.get_current_coltura()
        selected_id = self.ui.vista_selezione_coltura.get_current_coltura_id()
        num = self.controller.pianta_tutto(selected_id, self.time_thread.get_time())
        if num > 0:
            self.ui.error_label.setStyleSheet("color: #197d5a")
            self.controller.change_coltura(selected_id)
            self.ui.error_label.setText("piantando {} lotti".format(num))
            self.ui.label_coltura.setText("Coltura: {}".format(selected_text))
        else:
            self.ui.error_label.setStyleSheet("color: red")
            self.ui.error_label.setText("impossibile piantare lotti")

        self.clear_error_label = 1

    # Aggiorna icone e stato dei lotti e degli attuatori; pulisce il messaggio dopo qualche ciclo.
    def refresh_gui(self):
        time = self.time_thread.get_time()

        if self.clear_error_label == 2:
            self.ui.error_label.clear()

        if self.clear_error_label > 0:
            self.clear_error_label = (self.clear_error_label + 1)%3

        for label, id_lotto, status_lotto, salute_lotto, soglia_salute, fine in zip(
                                                                        self.ui.lotti,
                                                                        self.controller.get_id_lotti(),
                                                                        self.controller.get_status_lotti(),
                                                                        self.controller.get_salute_lotti(),
                                                                        self.controller.get_soglia_salute_lotti(),
                                                                        self.controller.get_date_fine()):
            name = "Lotto {}".format(id_lotto)

            self.ui.alert_frame_lotto[name].setStyleSheet("background-color: white")
            self.ui.alert_frame_lotto[name].setScaledContents(True)
            self.ui.alert_frame_lotto[name].setPixmap(self.img[status_lotto])

            if status_lotto == "coltivato" or status_lotto == "raccogliendo":
                label.setPixmap(self.full_lotto_img)
            else:
                label.setPixmap(self.empty_lotto_img)

            if status_lotto == "raccogliendo" or status_lotto == "piantando":
                self.ui.alert_frame_lotto[name].setPixmap(self.img[status_lotto])
            elif fine != "mancante" and time > datetime.strptime(fine,"%d %b %Y, %a %H:%M"):
                self.ui.alert_frame_lotto[name].setStyleSheet("background-color: yellow")
                self.ui.alert_frame_lotto[name].setPixmap(self.img['time_out'])
            elif status_lotto == 'coltivato' and salute_lotto < soglia_salute:
                self.ui.alert_frame_lotto[name].setStyleSheet("background-color: yellow")
                self.ui.alert_frame_lotto[name].setPixmap(self.img['ill'])

        self.ui.label_coltura.setText("Coltura: {}".format(self.controller.get_name_coltura()))

        if self.controller.is_pompa_on():
            self.ui.onoff_pompa.setPixmap(self.img["on"])
        else:
            self.ui.onoff_pompa.setPixmap(self.img["off"])

        if self.controller.is_serb_on():
            self.ui.onoff_co2.setPixmap(self.img["on"])
        else:
            self.ui.onoff_co2.setPixmap(self.img["off"])

        if self.controller.is_temp_reg_on():
            self.ui.onoff_temp_reg.setPixmap(self.img["on"])
        else:
            self.ui.onoff_temp_reg.setPixmap(self.img["off"])

        if self.controller.is_umid_on():
            self.ui.onoff_umid.setPixmap(self.img["on"])
        else:
            self.ui.onoff_umid.setPixmap(self.img["off"])

        if self.controller.is_pompa_oor():
            self.ui.alert_pompa.setPixmap(self.img["alert"])
            self.ui.alert_pompa.setStyleSheet("background-color: yellow")
        else:
            self.ui.alert_pompa.clear()
            self.ui.alert_pompa.setStyleSheet("background-color: transparent")

        if self.controller.is_serb_oor():
            self.ui.alert_co2.setPixmap(self.img["alert"])
            self.ui.alert_co2.setStyleSheet("background-color: yellow")
        else:
            self.ui.alert_co2.clear()
            self.ui.alert_co2.setStyleSheet("background-color: transparent")

        if self.controller.is_temp_reg_oor():
            self.ui.alert_temp_reg.setPixmap(self.img["alert"])
            self.ui.alert_temp_reg.setStyleSheet("background-color: yellow")
        else:
            self.ui.alert_temp_reg.clear()
            self.ui.alert_temp_reg.setStyleSheet("background-color: transparent")

        if self.controller.is_umid_oor():
            self.ui.alert_umid.setPixmap(self.img["alert"])
            self.ui.alert_umid.setStyleSheet("background-color: yellow")
        else:
            self.ui.alert_umid.clear()
            self.ui.alert_umid.setStyleSheet("background-color: transparent")

    # Apre la vista di dettaglio del lotto cliccato.
    def inspect_lotto(self,id,event):
        vista = Vista_Lotto(self,self.main_window,id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    # Apre la vista della pompa del settore.
    def inspect_pompa(self,event):
        vista = Vista_Pompa(self,self.main_window,self.id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    # Apre la vista dell'umidificatore del settore.
    def inspect_umid(self,event):
        id=self.controller.get_id_umid()
        vista = Vista_Umid(self,self.main_window,id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    # Apre la vista del regolatore di temperatura del settore.
    def inspect_temp_reg(self,event):
        id=self.controller.get_id_temp_reg()
        vista = Vista_Temp_Reg(self,self.main_window,id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    # Apre la vista del serbatoio di CO2 del settore.
    def inspect_co2(self,event):
        id=self.controller.get_id_serbCO2()
        vista = Vista_SerbCO2(self,self.main_window,id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    # Costruisce la UI, collega lotti e attuatori ai click e nasconde i comandi in modalità guest.
    def __init__(self,parent_ui,main_window, id):
        super().__init__()
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.id=id
        self.controller = Contr_Settore(id)

        self.ui = Ui_Settore()
        self.ui.setup_ui(self)

        self.start_time_refresher(self.ui.data_label)
        self.ui.frame_pompa.mousePressEvent = self.inspect_pompa
        self.ui.frame_co2.mousePressEvent = self.inspect_co2
        self.ui.frame_temp_reg.mousePressEvent = self.inspect_temp_reg
        self.ui.frame_umid.mousePressEvent = self.inspect_umid
        self.ui.indietro.clicked.connect(self.go_back)
        self.ui.button_raccogli.clicked.connect(self.raccogli_tutto)
        self.ui.button_pianta.clicked.connect(self.pianta_tutto)

        self.id_lotti = self.controller.get_id_lotti()
        numero_lotti = len(self.id_lotti)

        for i in range(numero_lotti):
            self.ui.lotti[i].mousePressEvent = partial(self.inspect_lotto,self.id_lotti[i])
            name = "Lotto {}".format(self.id_lotti[i])
            label = self.ui.lotti[i].findChildren(QLabel, "nome_lotto")[0]
            img_label = self.ui.lotti[i].findChildren(QLabel, "alert_frame_lotto")[0]
            img_label.setObjectName(name)
            self.ui.alert_frame_lotto[name] = img_label
            label.setText(name)

        self.load_imgs()
        self.clear_error_label = 0
        self.start_gui_refresher()

        if self.main_window.mode == "guest":
            self.ui.button_raccogli.hide()
            self.ui.button_pianta.hide()
            self.ui.vista_selezione_coltura.ui.combo_coltura.hide()
