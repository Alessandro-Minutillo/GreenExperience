from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.umid.model.lista_umid import Lista_Umid


# Controller dell'umidificatore: tramite tra vista e model.
class Contr_Umid(Contr_Att):
    def __init__(self,id):
        self.model = Lista_Umid().get_by_id(id)

    # Restituisce l'umidità obiettivo impostata.
    def get_umid_ob(self):
        return self.model.get_umid_ob()

    # Restituisce l'umidità consigliata per la coltura.
    def get_umid_cons(self):
        return self.model.get_umid_cons()

    # Imposta l'umidità obiettivo.
    def change_umid(self, val):
        self.model.change_umid(val)
