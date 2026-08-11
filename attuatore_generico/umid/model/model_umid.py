from attuatore_generico.interface.model_att import Model_Att
from colture.model.lista_colture import Lista_Colture


# Model dell'umidificatore: gestisce l'umidità obiettivo e il consumo energetico.
class Model_Umid(Model_Att):

    # Carica i dati dell'umidificatore e la coltura del settore associato.
    def __init__(self, id):
        super().__init__("Umid",id)
        id_coltura = self.retrieve_data("Settore", "id_coltura", "id_umid", self.id)["id_coltura"]
        self.coltura = Lista_Colture().get_by_id(id_coltura)

    # Restituisce l'umidità impostata come obiettivo.
    def get_umid_ob(self):
        return self.info["umid_ob"]

    # Restituisce l'umidità consigliata per la coltura piantata.
    def get_umid_cons(self):
        return self.coltura.get_umid_cons()

    # Imposta l'umidità obiettivo.
    def change_umid(self, val):
        self.info["umid_ob"] = val

    # Consumo reale: scala il consumo nominale in base allo scostamento dal valore consigliato.
    def get_consumo_real(self, spinbox_value):
        valore_finale=0
        if self.get_switch():
            cons_value = self.get_umid_cons()
            valore_finale=max(0,self.get_consumo()*(1 + (spinbox_value - cons_value)/cons_value))
        return valore_finale

    # True se l'umidità obiettivo differisce da quella consigliata.
    def is_oor(self):
        return self.get_umid_ob() != self.get_umid_cons()
