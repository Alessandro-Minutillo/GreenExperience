from colture.model.lista_colture import Lista_Colture
from attuatore_generico.interface.model_att import Model_Att


# Model del serbatoio di CO2: gestisce il livello obiettivo e il consumo energetico.
class Model_SerbCO2(Model_Att):

    # Carica i dati del serbatoio e la coltura del settore associato.
    def __init__(self, id):
        super().__init__("SerbCO2",id)
        id_coltura = self.retrieve_data("Settore", "id_coltura", "id_serbco2", self.id)["id_coltura"]
        self.coltura = Lista_Colture().get_by_id(id_coltura)

    # Restituisce il livello di CO2 impostato come obiettivo.
    def get_co2_ob(self):
        return self.info["liv_co2_ob"]

    # Restituisce il livello di CO2 consigliato per la coltura piantata.
    def get_co2_cons(self):
        return self.coltura.get_co2_cons()

    # Imposta il livello di CO2 obiettivo.
    def change_co2(self, val):
        self.info["liv_co2_ob"] = val

    # Consumo reale: scala il consumo nominale in base allo scostamento dal valore consigliato.
    def get_consumo_real(self, spinbox_value):
        valore_finale=0
        if self.get_switch():
            cons_value = self.get_co2_cons()
            valore_finale= max(0,self.get_consumo()*(1 + (spinbox_value - cons_value)/cons_value))
        return valore_finale

    # True se il livello obiettivo differisce da quello consigliato.
    def is_oor(self):
        return self.get_co2_ob() != self.get_co2_cons()
