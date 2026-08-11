from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2


# Controller del serbatoio di CO2: tramite tra Vista_SerbCO2 e Model_SerbCO2.
class Contr_SerbCO2(Contr_Att):

    def __init__(self,id):
        self.model = Lista_SerbCO2().get_by_id(id)

    # Restituisce il livello di CO2 obiettivo impostato.
    def get_co2_ob(self):
        return self.model.get_co2_ob()

    # Restituisce il livello di CO2 consigliato per la coltura.
    def get_co2_cons(self):
        return self.model.get_co2_cons()

    # Imposta il livello di CO2 obiettivo.
    def change_co2(self, val):
        self.model.change_co2(val)
