from attuatore_generico.interface.contr_att import Contr_Att
from attuatore_generico.luce_reg.model.lista_luce_reg import Lista_Luce_Reg

'''
    Implementazione della classe Contr_Luce_Reg
    Implementa il controller dell'impianto di illuminazione
'''

class Contr_Luce_Reg(Contr_Att):

    '''
        Costruttore
        Parametri:
            (int) id, id dell'impianto di illuminazione
        Percorso della funzione chiamata:
            util.lista.get_by_id(self,id)
    '''

    def __init__(self,id):
        self.model = Lista_Luce_Reg().get_by_id(id)
    
    '''
        Restituisce il tipo di luce attualmente impostato nell'impianto
        di illuminazione
        Percorso della funzione chiamata:
            attuatore_generico.luce_reg.model.model_luce_reg.get_luce(self)
        Return:
            (string) tipo di luce
    '''

    def get_luce(self):
        return self.model.get_luce()
    
    '''
        Setta il tipo di luce impostato nell'impianto di illuminazione
        Parametri: 
            (string) tipo di luce
        Percorso della funzione chiamata:
            attuatore_generico.luce_reg.model.model_luce_reg.change_luce(self, tipo)
    '''

    def change_luce(self, tipo):
        self.model.change_luce(tipo)