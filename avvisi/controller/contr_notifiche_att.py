from avvisi.model.model_notifiche_att import Model_Notifiche_Att


# Controller delle notifiche sugli attuatori: tramite verso Model_Notifiche_Att.
class Contr_Notifiche_Att():

    def __init__(self):
        self.model = Model_Notifiche_Att()

    # Dizionario dello stato spento/acceso delle pompe.
    def get_diz_pompa_off(self):
        return self.model.get_diz_pompa_off()

    # Dizionario dello stato spento/acceso degli impianti di illuminazione.
    def get_diz_luce_reg_off(self):
        return self.model.get_diz_luce_reg_off()

    # Dizionario dello stato spento/acceso dei regolatori di temperatura.
    def get_diz_temp_reg_off(self):
        return self.model.get_diz_temp_reg_off()

    # Dizionario dello stato spento/acceso degli umidificatori.
    def get_diz_umid_off(self):
        return self.model.get_diz_umid_off()

    # Dizionario dello stato spento/acceso dei serbatoi di CO2.
    def get_diz_serbco2_off(self):
        return self.model.get_diz_serbco2_off()

    # Dizionario dei fuori-range di funzionamento delle pompe.
    def get_diz_pompa_oor(self):
        return self.model.get_diz_pompa_oor()

    # Dizionario dei fuori-range degli impianti di illuminazione.
    def get_diz_luce_reg_oor(self):
        return self.model.get_diz_luce_reg_oor()

    # Dizionario dei fuori-range dei regolatori di temperatura.
    def get_diz_temp_reg_oor(self):
        return self.model.get_diz_temp_reg_oor()

    # Dizionario dei fuori-range degli umidificatori.
    def get_diz_umid_oor(self):
        return self.model.get_diz_umid_oor()

    # Dizionario dei fuori-range dei serbatoi di CO2.
    def get_diz_serbco2_oor(self):
        return self.model.get_diz_serbco2_oor()
