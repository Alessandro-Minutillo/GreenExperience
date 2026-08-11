from colture.model.lista_colture import Lista_Colture
from attuatore_generico.interface.model_att import Model_Att


# Model del regolatore di temperatura: gestisce la temperatura obiettivo e il consumo.
class Model_Temp_Reg(Model_Att):

    # Carica i dati del regolatore e la coltura del settore associato.
    def __init__(self, id):
        super().__init__("Temp_Reg",id)
        id_coltura = self.retrieve_data("Settore", "id_coltura", "id_temp_reg", self.id)["id_coltura"]
        self.coltura = Lista_Colture().get_by_id(id_coltura)

    # Restituisce la temperatura impostata come obiettivo.
    def get_temp_ob(self):
        return self.info["temp_ob"]

    # Restituisce la temperatura consigliata per la coltura piantata.
    def get_temp_cons(self):
        return self.coltura.get_temp_cons()

    # Imposta la temperatura obiettivo.
    def change_temp(self, val):
        self.info["temp_ob"] = val

    # Consumo reale: scala il consumo nominale in base allo scostamento dal valore consigliato.
    def get_consumo_real(self, spinbox_value):
        valore_finale=0
        if self.get_switch():
            cons_value = self.get_temp_cons()
            valore_finale= max(0,self.get_consumo()*(1 + (spinbox_value - cons_value)/cons_value))
        return valore_finale

    # True se la temperatura obiettivo differisce da quella consigliata.
    def is_oor(self):
        return self.get_temp_ob() != self.get_temp_cons()
