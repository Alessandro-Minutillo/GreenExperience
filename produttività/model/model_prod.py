from util.simple_model import Simple_Model
from datetime import datetime
import locale


# Model di un singolo prodotto raccolto (coltura, quantità, data).
class Model_Prod(Simple_Model):

    def __init__(self,id = None):
       super().__init__("Prodotto",id)
       locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")

    # Imposta la data del prodotto.
    def set_time(self,data):
        self.info["data"]=data

    # Restituisce la data di raccolta come datetime.
    def get_time(self):
        return (datetime.strptime(self.info["data"],"%d %b %Y, %a %H:%M"))

    # Restituisce l'id della coltura del prodotto.
    def get_id_coltura(self):
        return (self.info["id_coltura"])

    # Restituisce la quantità prodotta (kg).
    def get_quant(self):
        return (self.info["quant"])

    # Popola un nuovo record di prodotto con i valori forniti.
    def set_new_model(self, id, id_lotto, id_coltura, quant, data):
        self.id = id
        self.info["id"] = id
        self.info["id_lotto"] = id_lotto
        self.info["id_coltura"] = id_coltura
        self.info["quant"] = quant
        self.info["data"] = data
