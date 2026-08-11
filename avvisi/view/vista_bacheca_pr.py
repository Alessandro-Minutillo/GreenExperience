from avvisi.view.notifica_vuota import Notifica_Vuota
from avvisi.view.vista_bacheca import Vista_Bacheca
from avvisi.view.notifica_pianta import Notifica_Pianta
from avvisi.controller.contr_notifiche_lotto import Contr_Notifiche_Lotto
from avvisi.view.notifica_raccolta import Notifica_Raccolta


# Bacheca delle notifiche per piantare i lotti vuoti e raccogliere quelli scaduti.
class Vista_Bacheca_PR(Vista_Bacheca):

    # Costruisce la bacheca e avvia il refresh.
    def __init__(self, parent_ui, main_window):
        super().__init__(parent_ui, main_window, "Pianta e Raccogli")
        self.controller = Contr_Notifiche_Lotto()
        self.start_gui_refresher()

    # Sincronizza le notifiche di raccolta e piantumazione con lo stato corrente dei lotti.
    def refresh_gui(self):
        time = self.parent_ui.time_thread.get_time()
        diz_1 = self.controller.get_diz_time_out_lotti(time)
        diz_2 = self.controller.get_diz_lotti_vuoti()
        deleted = 0

        for i in range(self.ui.list_notify.count()):

            item = self.ui.list_notify.item(i-deleted)
            widget = self.ui.list_notify.itemWidget(item)
            type = widget.__class__

            if type == Notifica_Raccolta:
                id = widget.get_id()
                if not diz_1[id]:
                    self.ui.list_notify.takeItem(i-deleted)
                    deleted += 1
                del diz_1[id]
            elif type == Notifica_Pianta:
                id = widget.get_id()
                if not diz_2[id]:
                    self.ui.list_notify.takeItem(i-deleted)
                    deleted += 1
                del diz_2[id]
            elif type == Notifica_Vuota:
                self.ui.list_notify.takeItem(i-deleted)
                deleted += 1

        for id, flag in diz_1.items():
            if flag:
                self.add_widget(Notifica_Raccolta(self,self.main_window, id))

        for id, flag in diz_2.items():
            if flag:
                self.add_widget(Notifica_Pianta(self,self.main_window, id))

        self.fill_empty_list()
