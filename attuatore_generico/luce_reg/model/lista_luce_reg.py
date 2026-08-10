from attuatore_generico.interface.lista_att import Lista_Att
from attuatore_generico.luce_reg.model.model_luce_reg import Model_Luce_Reg
from util.singleton import Singleton

'''
    Implementazione della classe Lista_Luce_Reg
    Definisce una lista di impianti di illuminazione
'''

@Singleton
class Lista_Luce_Reg(Lista_Att):
    
    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__(Model_Luce_Reg, "Luce_Reg")