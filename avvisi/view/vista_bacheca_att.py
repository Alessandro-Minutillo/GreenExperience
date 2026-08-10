from avvisi.view.notifica_vuota import Notifica_Vuota
from avvisi.view.notifica_att import Notifica_Att
from avvisi.view.notifica_on_off import Notifica_On_Off
from avvisi.controller.contr_notifiche_att import Contr_Notifiche_Att
from avvisi.view.vista_bacheca import Vista_Bacheca

'''
    Implementazione della classe Vista_Bacheca_Att
    Implementa la vista della bacheca dedicata alle notifiche
    riguardanti gli attuatori
'''

class Vista_Bacheca_Att(Vista_Bacheca):

    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            avvisi.view.vista_bacheca.start_gui_refresher(self)
    '''

    def __init__(self, parent_ui, main_window):
        super().__init__(parent_ui, main_window, "Controlla gli attuatori")
        self.controller = Contr_Notifiche_Att()
        self.start_gui_refresher()

    '''
        Esegue il refresh della gui
        E' connessa al segnale emesso dal QThread Gui_Refresher
        istanziato da util.simple_window.start_gui_refresher(self)

        Percorso delle funzioni chiamate:
            avvisi.controller.contr_notifiche_att.get_diz_temp_reg_off(self)
            avvisi.controller.contr_notifiche_att.get_diz_luce_reg_off(self)
            avvisi.controller.contr_notifiche_att.get_diz_umid_off(self)
            avvisi.controller.contr_notifiche_att.get_diz_pompa_off(self)
            avvisi.controller.contr_notifiche_att.get_diz_luce_reg_oor(self)
            avvisi.controller.contr_notifiche_att.get_diz_temp_reg_oor(self)
            avvisi.controller.contr_notifiche_att.get_diz_umid_oor(self)
            avvisi.controller.contr_notifiche_att.get_diz_pompa_oor(self)
            avvisi.view.vista_bacheca.add_widget(self,widget)
            avvisi.view.vista_bacheca.fill_empty_list(self)
    '''

    def refresh_gui(self):
        diz_0 = self.controller.get_diz_temp_reg_off()
        diz_1 = self.controller.get_diz_temp_reg_oor()
        diz_2 = self.controller.get_diz_luce_reg_off()
        diz_3 = self.controller.get_diz_luce_reg_oor()
        diz_4 = self.controller.get_diz_umid_off()
        diz_5 = self.controller.get_diz_umid_oor()
        diz_6 = self.controller.get_diz_serbco2_off()
        diz_7 = self.controller.get_diz_serbco2_oor()
        diz_8 = self.controller.get_diz_pompa_off()
        diz_9 = self.controller.get_diz_pompa_oor()

        nome_diz_on_off = {}
        nome_diz_att = {}

        nome_diz_on_off["temp_reg"] = diz_0
        nome_diz_on_off["luce_reg"] = diz_2
        nome_diz_on_off["umid"] = diz_4
        nome_diz_on_off["serb_co2"] = diz_6
        nome_diz_on_off["pompa"] = diz_8

        nome_diz_att["temp_reg"] = diz_1
        nome_diz_att["luce_reg"] = diz_3
        nome_diz_att["umid"] = diz_5
        nome_diz_att["serb_co2"] = diz_7
        nome_diz_att["pompa"] = diz_9

        deleted = 0

        for i in range(self.ui.list_notify.count()):
            
            item = self.ui.list_notify.item(i-deleted)
            widget = self.ui.list_notify.itemWidget(item)
            type = widget.__class__

            if type == Notifica_On_Off:
                id = widget.get_id()
                nome_att = widget.get_nome_att()
                if not nome_diz_on_off[nome_att][id]:
                    self.ui.list_notify.takeItem(i-deleted)
                    deleted += 1
                del nome_diz_on_off[nome_att][id]
            elif type == Notifica_Att:
                id = widget.get_id()
                nome_att = widget.get_nome_att()
                if not nome_diz_att[nome_att][id]:
                    self.ui.list_notify.takeItem(i-deleted)
                    deleted += 1
                del nome_diz_att[nome_att][id]
            elif type == Notifica_Vuota:
                self.ui.list_notify.takeItem(i-deleted)
                deleted += 1
        
        for nome_att, diz in nome_diz_on_off.items():
            for id, flag in diz.items():
                if flag:
                    self.add_widget(Notifica_On_Off(self,self.main_window, id, nome_att))
        
        for nome_att, diz in nome_diz_att.items():
            for id, flag in diz.items():
                if flag:
                    self.add_widget(Notifica_Att(self,self.main_window, id, nome_att))
        
        self.fill_empty_list()