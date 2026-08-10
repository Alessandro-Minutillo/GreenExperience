from avvisi.view.notifica_vuota import Notifica_Vuota
from avvisi.view.notifica_lotto import Notifica_Lotto
from avvisi.view.vista_bacheca import Vista_Bacheca
from avvisi.controller.contr_notifiche_lotto import Contr_Notifiche_Lotto

'''
    Implementazione della classe Vista_Bacheca_SL
    Implementa la vista della bacheca dedicata alle notifiche
    riguardanti lo stato di salute dei lotti
'''

class Vista_Bacheca_SL(Vista_Bacheca):

    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            avvisi.view.vista_bacheca.start_gui_refresher(self)
    '''

    def __init__(self, parent_ui, main_window):
        super().__init__(parent_ui, main_window, "Controlla i lotti")
        self.controller = Contr_Notifiche_Lotto()
        self.start_gui_refresher()

    '''
        Esegue il refresh della gui
        E' connessa al segnale emesso dal QThread Gui_Refresher
        istanziato da util.simple_window.start_gui_refresher(self)

        Percorso delle funzioni chiamate:
            avvisi.controller.contr_notifiche_lotto.get_diz_low_salute_lotti(self)
            avvisi.view.vista_bacheca.add_widget(self,widget)
            avvisi.view.vista_bacheca.fill_empty_list(self)
    '''

    def refresh_gui(self):
        diz = self.controller.get_diz_low_salute_lotti()
        deleted = 0

        for i in range(self.ui.list_notify.count()):
            
            item = self.ui.list_notify.item(i-deleted)
            widget = self.ui.list_notify.itemWidget(item)
            type = widget.__class__

            if type == Notifica_Lotto:
                id = widget.get_id()
                flag, salute = diz[id]
                if not flag or int(salute) != int(widget.get_salute()):
                    self.ui.list_notify.takeItem(i-deleted)
                    deleted += 1
                if not flag or int(salute) == int(widget.get_salute()):
                    del diz[id]
            elif type == Notifica_Vuota:
                self.ui.list_notify.takeItem(i-deleted)
                deleted += 1
        
        for id, item in diz.items():
            flag, salute = item
            if flag:
                self.add_widget(Notifica_Lotto(self,self.main_window, id, self.controller.get_id_settore(id), salute))
        
        self.fill_empty_list()