from attuatore_generico.interface.model_att import Model_Att

'''
    Implementazione della classe Model_Att
    Implementa il model dell'impianto di illuminazione
'''

class Model_Luce_Reg(Model_Att):

    '''
        Costruttore
        Parametri: (int) id, id dell'impianto di illuminazione
    '''

    def __init__(self, id):
        super().__init__("Luce_Reg",id)
    
    '''
        Restituisce il tipo di luce attualmente 
        impostato nell'impianto di illuminazione
        Return: (string) tipo luce
    
    '''

    def get_luce(self):
        return self.info["luce"]

    '''
        Setta il tipo di luce impostato nell'impianto di illuminazione
        Parametri: 
            (string) tipo, tipo di luce
    '''

    def change_luce(self,tipo):
        self.info["luce"] = tipo