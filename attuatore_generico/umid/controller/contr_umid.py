from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.umid.model.lista_umid import Lista_Umid

"""
    Implementazione della classe Contr_Umid
    Eredita dalla classe Contr_Att
    Contiene i richiami delle funzioni definite nella classe Model_Umid
    Costituisce il tramite tra la classe Model_Umid e la classe Vista_Umid

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""

class Contr_Umid(Contr_Att):
    def __init__(self,id):
        self.model = Lista_Umid().get_by_id(id)

    """
        Restituisce il risultato della funzione get_umid_ob() presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.umid.model.get_umid_ob()
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui è attualmente impostato l'attuatore
    """
    def get_umid_ob(self):
        return self.model.get_umid_ob()

    """
        Restituisce il risultato della funzione get_umid_cons() presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.umid.model.get_umid_cons()
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui sarebbe corretto impostare l'attuatore
            a seconda della coltura coltivata
    """
    def get_umid_cons(self):
        return self.model.get_umid_cons()
    
    """
        Esegue la funzione change_umid(val) presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.umid.model.change_umid()
        Parametri:
            val: Decimale rappresentante il valore presente nella spinbox inserito dall'utente
        Return:
            Nessuno
    """
    def change_umid(self, val):
        self.model.change_umid(val)