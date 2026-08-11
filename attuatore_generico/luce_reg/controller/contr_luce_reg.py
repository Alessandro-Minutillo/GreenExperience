from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.luce_reg.model.lista_luce_reg import Lista_Luce_Reg


# Controller dell'impianto di illuminazione: tramite tra vista e model.
class Contr_Luce_Reg(Contr_Att):

    def __init__(self,id):
        self.model = Lista_Luce_Reg().get_by_id(id)

    # Restituisce il tipo di luce impostato.
    def get_luce(self):
        return self.model.get_luce()

    # Imposta il tipo di luce dell'impianto.
    def change_luce(self, tipo):
        self.model.change_luce(tipo)
