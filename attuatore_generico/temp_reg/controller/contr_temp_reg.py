from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg

"""
    Implementazione della classe Contr_Temp_Reg
    Eredita dalla classe Contr_Att
    Contiene i richiami delle funzioni definite nella classe Model_Temp_Reg
    Costituisce il tramite tra la classe Model_Temp_Reg e la classe Vista_Temp_Reg

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""

class Contr_Temp_Reg(Contr_Att):
    def __init__(self, id):
        self.model = Lista_Temp_Reg().get_by_id(id)
    
    """
        Restituisce il risultato della funzione get_temp_ob() presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.temp_reg.model.get_temp_ob()
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui è attualmente impostato l'attuatore
    """
    def get_temp_ob(self):
        return self.model.get_temp_ob()

    """
        Restituisce il risultato della funzione get_temp_cons() presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.temp_reg.model.get_temp_cons()
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui sarebbe corretto impostare l'attuatore
            a seconda della coltura coltivata
    """
    def get_temp_cons(self):
        return self.model.get_temp_cons()
        
    """
        Esegue la funzione change_temp(val) presente nel model
        Percorso della funzione richiamata:
            attuatore_generico.temp_reg.model.change_temp()
        Parametri:
            val: Decimale rappresentante il valore presente nella spinbox inserito dall'utente
        Return:
            Nessuno
    """
    def change_temp(self, val):
        self.model.change_temp(val)