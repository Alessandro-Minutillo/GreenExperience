from util.simple_model import Simple_Model


# Model di un consumo unitario (idrico ed elettrico) campionato in una data.
class Model_Consumo(Simple_Model):
    def __init__(self,id = None):
        super().__init__("Consumo",id)

    # Popola un nuovo record di consumo con i valori forniti.
    def set_new_model(self, id, id_serra ,consumo_idrico, consumo_elettrico, data):
        self.id = id
        self.info["id"] = id
        self.info["id_serra"] = id_serra
        self.info["consumo_idrico"] = consumo_idrico
        self.info["consumo_elettrico"] = consumo_elettrico
        self.info["data"] = data
