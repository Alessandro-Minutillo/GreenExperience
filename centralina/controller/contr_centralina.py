from centralina.model.lista_centraline import Lista_Centraline


# Controller della centralina: tramite tra la vista e Model_Centralina.
class Contr_Centralina():

    def __init__(self,id):
        self.model = Lista_Centraline().get_by_id(id)

    # Temperatura rilevata, formattata a un decimale.
    def get_temp(self):
        return "{:.1f}".format(self.model.get_temp())

    # Concentrazione di CO2 rilevata, formattata senza decimali.
    def get_liv_co2(self):
        return "{:.0f}".format(self.model.get_liv_co2())

    # Umidità rilevata, formattata a un decimale.
    def get_umid(self):
        return "{:.1f}".format(self.model.get_umid())

    # Restituisce il model della centralina.
    def get_model(self):
        return self.model
