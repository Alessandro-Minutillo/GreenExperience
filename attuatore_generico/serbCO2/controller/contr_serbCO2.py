from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2

"""
    Implementazione della classe Contr_SerbCO2
    Eredita dalla classe Contr_Att
    Contiene i richiami delle funzioni definite nella classe Model_SerbCO2
    Costituisce il tramite tra la classe Model_SerbCO2 e la classe Vista_SerbCO2

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""

class Contr_SerbCO2(Contr_Att):

    def __init__(self,id):
        self.model = Lista_SerbCO2().get_by_id(id)
        
    """
        Restituisce il risultato della funzione get_co2_ob() presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.serbCO2.model.get_co2_ob()
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui è attualmente impostato l'attuatore
    """
    def get_co2_ob(self):
        return self.model.get_co2_ob()

    """
        Restituisce il risultato della funzione get_co2_cons() presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.serbCO2.model.get_co2_cons()
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui sarebbe corretto impostare l'attuatore
            a seconda della coltura coltivata
    """
    def get_co2_cons(self):
        return self.model.get_co2_cons()
        
    """
        Esegue la funzione change_co2(val) presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.serbCO2.model.change_co2()
        Parametri:
            val: Decimale rappresentante il valore presente nella spinbox inserito dall'utente
        Return:
            Nessuno
    """
    def change_co2(self, val):
        self.model.change_co2(val)