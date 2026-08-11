from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg


# Controller del regolatore di temperatura: tramite tra vista e model.
class Contr_Temp_Reg(Contr_Att):
    def __init__(self, id):
        self.model = Lista_Temp_Reg().get_by_id(id)

    # Restituisce la temperatura obiettivo impostata.
    def get_temp_ob(self):
        return self.model.get_temp_ob()

    # Restituisce la temperatura consigliata per la coltura.
    def get_temp_cons(self):
        return self.model.get_temp_cons()

    # Imposta la temperatura obiettivo.
    def change_temp(self, val):
        self.model.change_temp(val)
