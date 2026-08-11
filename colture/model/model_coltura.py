from util.simple_model import Simple_Model
from colture.model.lista_profili_luce import Lista_Profili_Luce
from colture.model.lista_soluzioni import Lista_Soluzioni


# Model di una coltura: parametri agronomici consigliati, soluzione e profilo luce.
class Model_Coltura(Simple_Model):

    # Carica i dati della coltura e le relative soluzione e profilo luce.
    def __init__(self, id):
        super().__init__("Coltura",id)
        id_soluzione = self.info["id_soluzione_circolante"]
        id_profilo_luce = self.info["id_profilo_luce"]
        self.soluzione = Lista_Soluzioni().get_by_id(id_soluzione)
        self.profilo_luce = Lista_Profili_Luce().get_by_id(id_profilo_luce)

    # Restituisce il nome comune della coltura.
    def get_name(self):
        return self.info["nome_comune"]

    # Restituisce il pH consigliato.
    def get_ph_cons(self):
        return self.info["pH_cons"]

    # Restituisce l'EC (salinità) consigliata.
    def get_ec_cons(self):
        return self.info["ec_cons"]

    # Restituisce la durata media del ciclo colturale (giorni).
    def get_durata(self):
        return int(self.info["durata"])

    # Restituisce la temperatura consigliata.
    def get_temp_cons(self):
        return self.info["temp_cons"]

    # Restituisce l'umidità consigliata.
    def get_umid_cons(self):
        return self.info["umid_cons"]

    # Restituisce la concentrazione di CO2 consigliata.
    def get_co2_cons(self):
        return self.info["liv_co2_cons"]

    # Restituisce la resa per lotto.
    def get_prod_per_lotto(self):
        return int(self.info["prod_lotto"])

    # Restituisce la soluzione circolante formattata (HTML).
    def get_soluzione(self):
        return str(self.soluzione)

    # Restituisce l'oggetto Model_Soluzione della coltura.
    def get_raw_sol(self):
        return self.soluzione

    # Restituisce il profilo luce formattato (HTML).
    def get_profilo_luce(self):
        return str(self.profilo_luce)
