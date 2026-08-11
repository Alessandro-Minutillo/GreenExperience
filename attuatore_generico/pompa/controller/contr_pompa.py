from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from attuatore_generico.interface.contr_att import Contr_Att


# Controller della pompa: tramite tra Vista_Pompa e Model_Pompa.
class Contr_pompa(Contr_Att):
    def __init__(self,id):
        self.id=id
        self.model = Lista_Pompe().get_by_id(id)

    # Imposta la salinità (EC) della soluzione circolante.
    def on_change_ec(self,value):
        self.model.on_change_ec(value)

    # Imposta il pH della soluzione circolante.
    def on_change_ph(self,value):
        self.model.on_change_ph(value)

    # Imposta il profilo della soluzione circolante.
    def on_change_sol(self,index):
        self.model.on_change_sol(index)

    # Restituisce la salinità (EC) della soluzione.
    def get_ec(self):
        return self.model.get_ec()

    # Restituisce il pH della soluzione.
    def get_ph(self):
        return self.model.get_ph()

    # Restituisce il consumo elettrico orario della pompa.
    def get_consumo_el(self):
        return self.model.get_consumo_el()

    # Restituisce il consumo idrico orario della pompa.
    def get_consumo_idro(self):
        return self.model.get_consumo_idro()

    # Restituisce la soluzione circolante attuale.
    def get_sol(self):
        return self.model.get_sol()

    # Restituisce la soluzione circolante consigliata.
    def get_sol_cons(self):
        return self.model.get_sol_cons()

    # Restituisce il pH consigliato.
    def get_ph_cons(self):
        return self.model.get_ph_cons()

    # Restituisce la salinità (EC) consigliata.
    def get_ec_cons(self):
        return self.model.get_ec_cons()

    # Restituisce l'elenco dei profili soluzione disponibili.
    def get_list_profiles(self):
        return self.model.get_list_profiles()
