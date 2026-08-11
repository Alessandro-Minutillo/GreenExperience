from lotto.model.lista_lotti import Lista_Lotti
from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg
from attuatore_generico.umid.model.lista_umid import Lista_Umid
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2


# Model delle notifiche sugli attuatori: raccoglie stato e fuori-range da tutte le liste.
class Model_Notifiche_Att():

    def __init__(self):
        self.pompe = Lista_Pompe()
        self.lotti = Lista_Lotti()
        self.temp_reg = Lista_Temp_Reg()
        self.umid = Lista_Umid()
        self.serbco2 = Lista_SerbCO2()

    # Dizionario dello stato spento/acceso delle pompe.
    def get_diz_pompa_off(self):
        return self.pompe.get_diz_off()

    # Dizionario dello stato spento/acceso degli impianti di illuminazione (per lotto).
    def get_diz_luce_reg_off(self):
        return self.lotti.get_diz_off()

    # Dizionario dello stato spento/acceso dei regolatori di temperatura.
    def get_diz_temp_reg_off(self):
        return self.temp_reg.get_diz_off()

    # Dizionario dello stato spento/acceso degli umidificatori.
    def get_diz_umid_off(self):
        return self.umid.get_diz_off()

    # Dizionario dello stato spento/acceso dei serbatoi di CO2.
    def get_diz_serbco2_off(self):
        return self.serbco2.get_diz_off()

    # Dizionario dei fuori-range di funzionamento delle pompe.
    def get_diz_pompa_oor(self):
        return self.pompe.get_diz_oor()

    # Dizionario dei fuori-range degli impianti di illuminazione (per lotto).
    def get_diz_luce_reg_oor(self):
        return self.lotti.get_diz_oor()

    # Dizionario dei fuori-range dei regolatori di temperatura.
    def get_diz_temp_reg_oor(self):
        return self.temp_reg.get_diz_oor()

    # Dizionario dei fuori-range degli umidificatori.
    def get_diz_umid_oor(self):
        return self.umid.get_diz_oor()

    # Dizionario dei fuori-range dei serbatoi di CO2.
    def get_diz_serbco2_oor(self):
        return self.serbco2.get_diz_oor()
