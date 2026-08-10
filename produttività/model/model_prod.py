from util.simple_model import Simple_Model
from datetime import datetime
import locale
'''
    Implementazionde della classe Model_Prod
    Implementa un model che rappresenta il singolo prodotto
'''
class Model_Prod(Simple_Model):
    '''
        Costruttore
        Parametri:
            Nessuno
        Return:
            Nessuno
    '''
    def __init__(self,id = None):
       super().__init__("Prodotto",id)
       locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
    '''
        Inserisce nelle info il valore della data di un singolo prodotto
        Parametri:
            (datetime) data: la data da inserire  
        Return:
            Nessuno
    '''
    def set_time(self,data):
        self.info["data"]=data
    '''
        Restituisce la data in cui il singolo prodotto è stato raccolto
        Parametri:
            Nessuno
        Return
            (datetime) data
    '''
    def get_time(self):
        return (datetime.strptime(self.info["data"],"%d %b %Y, %a %H:%M"))
    '''
        Restituisce l'id della coltura
        Parametri:
            Nessuno
        Return
            (int) id coltura
    '''
    def get_id_coltura(self):
        return (self.info["id_coltura"])
    '''
        restituisce la quantità prodotta
        Parametri:
            Nessuno
        Return
            (int) quantità di proddotto ricavanta,in kg
    '''
    def get_quant(self):
        return (self.info["quant"])
    '''
        Istanzia un nuovo ogetto "prodotto"
        Parametri:
            (int) id: l'id relativo al prodotto
            (int) id_lotto: l'id del lotto relativo al prodotto
            (int) id_coltura: l'id della coltura
            (int) quant: quantità di  prodotto raccolta 
            (datetime) data: data di raccolta del prodotto
        Return:
            Nessuno
    '''
    def set_new_model(self, id, id_lotto, id_coltura, quant, data):
        self.id = id
        self.info["id"] = id
        self.info["id_lotto"] = id_lotto
        self.info["id_coltura"] = id_coltura
        self.info["quant"] = quant
        self.info["data"] = data
