from util.simple_model import Simple_Model

"""
    Implementazione della classe Model_Consumo

    Contiene i dati che rappresentano un consumo unitario

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Model_Consumo(Simple_Model):
    def __init__(self,id = None):
        super().__init__("Consumo",id)

    """
        Crea un nuovo consumo utilizzando i parametri forniti
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            id: l' id del nuovo consumo (int)
            id_serra: l' id della serra corrispondente (int)
            consumo_idrico: la quantità di litri di soluzione consumati (float)
            consumo_elettrico: il numero di KWh consumati (float)
            data: la data del campionamento del consumo (string)
        Return:
            Nessuno
    """
    def set_new_model(self, id, id_serra ,consumo_idrico, consumo_elettrico, data):
        self.id = id
        self.info["id"] = id
        self.info["id_serra"] = id_serra
        self.info["consumo_idrico"] = consumo_idrico
        self.info["consumo_elettrico"] = consumo_elettrico
        self.info["data"] = data
